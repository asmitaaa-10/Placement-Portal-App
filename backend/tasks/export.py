import csv
import io

from celery import shared_task
from backend.extensions import db
from backend.models import Application, PlacementDrive, User


@shared_task(name="export_applications_csv")
def export_applications_csv(drive_id=None):
    """
    Exports applications to CSV and emails it to the admin.
    Optionally filter by drive_id.
    """

    query = db.session.query(
        Application.id,
        User.username,
        User.email,
        PlacementDrive.title,
        Application.status,
        Application.applied_at
    ).join(User, Application.student_id == User.id)\
     .join(PlacementDrive, Application.drive_id == PlacementDrive.id)

    if drive_id:
        query = query.filter(Application.drive_id == drive_id)

    applications = query.all()

    # Build CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Application ID", "Student Name", "Email", "Drive", "Status", "Applied At"])

    for app in applications:
        writer.writerow([
            app.id,
            app.username,
            app.email,
            app.title,
            app.status,
            app.applied_at.strftime("%Y-%m-%d %H:%M:%S") if app.applied_at else ""
        ])

    csv_content = output.getvalue()
    output.close()

    # Email CSV to admin
    from backend.utils.mail import sendMail
    admin = User.query.filter_by(role="admin").first()

    if admin:
        sendMail(
            to=admin.email,
            subject="Applications Export - CSV Report",
            body=csv_content
        )

    return {"exported": len(applications)}