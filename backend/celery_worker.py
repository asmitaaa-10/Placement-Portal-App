# celery_worker.py
from celery import Celery

celery_app = Celery(
    'my_app',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)