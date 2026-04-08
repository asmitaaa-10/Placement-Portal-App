
from backend.app import create_app
from backend.tasks import generate_monthly_report, export_applications_csv, send_deadline_reminders

flask_app = create_app()
celery_app = flask_app.extensions['celery']