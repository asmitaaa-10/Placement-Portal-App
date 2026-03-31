from datetime import datetime, timedelta, timezone
from celery import shared_task
from backend.extensions import db
from backend.models import PlacementDrive, Application, StudentProfile, User
from backend.utils.mail import sendMail


@shared_task(name="send_deadline_reminders")
def send_deadline_reminders():
    """
    Sends email reminders to students about drives whose deadline
    is within the next 2 days and they haven't applied yet.
    """

    now = datetime.now(timezone.utc)
    reminder_window = now + timedelta(days=3)

    # Get drives with deadlines in the next 2 days that are still open
    upcoming_drives = PlacementDrive.query.filter(
        PlacementDrive.application_deadline >= now,
        PlacementDrive.application_deadline <= reminder_window,
        PlacementDrive.status == "Approved"
    ).all()

    if not upcoming_drives:
        return {"msg": "No upcoming deadlines found", "reminders_sent": 0}

    reminders_sent = 0

    # Get all active students
    students = StudentProfile.query.join(User).filter(
        User.active_flag == True,
        User.blacklist_flag == False
    ).all()

    for student in students:
        user = User.query.get(student.user_id)
        if not user or not user.email:
            continue

        # Find drives this student hasn't applied to yet
        applied_drive_ids = [
            a.drive_id for a in Application.query.filter_by(student_id=student.id).all()
        ]

        not_applied_drives = [
            d for d in upcoming_drives if d.id not in applied_drive_ids
        ]

        if not not_applied_drives:
            continue

        # Build email
        drive_list_html = ""
        for drive in not_applied_drives:
            deadline_str = drive.application_deadline.strftime('%d %b %Y, %I:%M %p UTC')
            drive_list_html += f"""
            <div style="border:1px solid #ddd; border-radius:6px; padding:12px; margin-bottom:10px;">
                <strong>{drive.job_title}</strong><br>
                <span style="color:#e74c3c;">Deadline: {deadline_str}</span>
            </div>
            """

        html_body = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; background: #f5f5f5; margin: 0; padding: 20px; }}
        .container {{ background: white; padding: 30px; border-radius: 8px; max-width: 600px; margin: auto; }}
        h2 {{ color: #2c3e50; }}
        .footer {{ margin-top: 20px; color: #999; font-size: 12px; }}
        .btn {{ background: #3498db; color: white; padding: 10px 20px; text-decoration: none; border-radius: 4px; }}
    </style>
</head>
<body>
    <div class="container">
        <h2>⏰ Upcoming Application Deadlines</h2>
        <p>Hi <strong>{user.username}</strong>,</p>
        <p>The following placement drives are closing soon. Don't miss out!</p>
        {drive_list_html}
        <p>Log in to the Placement Portal to apply before the deadline.</p>
        <div class="footer">-- Placement Portal | Daily Reminder</div>
    </div>
</body>
</html>
"""

        try:
            sendMail(
                to=user.email,
                subject="⏰ Reminder: Upcoming Placement Drive Deadlines",
                body=html_body
            )
            reminders_sent += 1
        except Exception as e:
            print(f"Failed to send reminder to {user.email}: {e}")

    return {"reminders_sent": reminders_sent}