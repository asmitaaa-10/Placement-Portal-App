from celery.schedules import crontab

broker_url = "redis://localhost:6379/0"
result_backend = "redis://localhost:6379/0"

beat_schedule = {
    "monthly-placement-report": {
        "task": "generate_monthly_report",
        "schedule": crontab(
            minute=0,
            hour=9,
            day_of_month=1
        ),
    },

    "daily-deadline-reminders": {
        "task": "send_deadline_reminders",
        "schedule": crontab(minute=0, hour=8),  # Every day at 8:00 AM IST
    },
}

timezone = "Asia/Kolkata"
