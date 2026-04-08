import os
from datetime import datetime
from sqlalchemy import func
from flask import current_app
from celery import shared_task

from backend.extensions import db
from backend.models import PlacementDrive, Application, User
from backend.utils.mail import sendMail

import glob

def generate_html_report(start_date, drives_count, students_applied, students_selected):
    month_label = start_date.strftime('%B %Y')
    generated_on = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

    css = """
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        .container { background: white; padding: 30px; border-radius: 8px; max-width: 600px; margin: auto; }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        .stat { display: flex; justify-content: space-between; padding: 15px 0; border-bottom: 1px solid #eee; }
        .stat-label { color: #555; font-size: 16px; }
        .stat-value { font-size: 24px; font-weight: bold; color: #3498db; }
        .footer { margin-top: 30px; color: #999; font-size: 12px; text-align: center; }
    </style>
    """

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Monthly Placement Report - {month_label}</title>
    {css}
</head>
<body>
    <div class="container">
        <h1>Monthly Placement Activity Report</h1>
        <p><strong>Month:</strong> {month_label}</p>
        <p><strong>Generated on:</strong> {generated_on}</p>
        <div class="stat">
            <span class="stat-label">Drives Conducted</span>
            <span class="stat-value">{drives_count}</span>
        </div>
        <div class="stat">
            <span class="stat-label">Students Applied</span>
            <span class="stat-value">{students_applied}</span>
        </div>
        <div class="stat">
            <span class="stat-label">Students Selected</span>
            <span class="stat-value">{students_selected}</span>
        </div>
        <div class="footer">-- Placement Portal | Auto-generated report</div>
    </div>
</body>
</html>"""

    return html


@shared_task(name="generate_monthly_report")
def generate_monthly_report():

    today = datetime.utcnow()


    # start_date = datetime(last_day_previous_month.year, last_day_previous_month.month, 1)
    # end_date = datetime(
    #     last_day_previous_month.year,
    #     last_day_previous_month.month,
    #     last_day_previous_month.day,
    #     23, 59, 59
    # )

    start_date = datetime(today.year, today.month, 1)
    end_date = today

    drives_count = db.session.query(func.count(PlacementDrive.id))\
        .filter(PlacementDrive.created_at.between(start_date, end_date)).scalar()

    students_applied = db.session.query(func.count(Application.id))\
        .filter(Application.application_date.between(start_date, end_date)).scalar()  # ✅ fixed

    students_selected = db.session.query(func.count(Application.id))\
        .filter(
            Application.status == "Selected",   
            Application.updated_at.between(start_date, end_date)
        ).scalar()

    html_content = generate_html_report(start_date, drives_count, students_applied, students_selected)
    filename = f"Monthly_Report_{today.strftime('%Y_%m')}.html"

    uploads_dir = os.path.join(current_app.config['BASE_DIR'], 'uploads')
    os.makedirs(uploads_dir, exist_ok=True)

    old_reports = glob.glob(os.path.join(uploads_dir, 'Monthly_Report_*.html'))
    for old_file in old_reports:
        os.remove(old_file)

    filepath = os.path.join(uploads_dir, filename)
    with open(filepath, 'w') as f:
        f.write(html_content)

    subject = f"Placement Report - {start_date.strftime('%B %Y')}"
    admin = User.query.filter_by(role="Admin").first()  
    if admin:
        sendMail(
            to=admin.email,
            subject=subject,
            body=html_content
        )

    return {
        "drives": drives_count,
        "applied": students_applied,
        "selected": students_selected,
        "report": filename
    }