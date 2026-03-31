# # celery_worker.py
# from celery import Celery

# celery_app = Celery(
#     'my_app',
#     broker='redis://localhost:6379/0',
#     backend='redis://localhost:6379/0'
# )

from backend.app import create_app
from backend.tasks import generate_monthly_report, export_applications_csv

flask_app = create_app()
celery_app = flask_app.extensions['celery']