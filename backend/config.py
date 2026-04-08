import os
from datetime import timedelta
from celery.schedules import crontab


class Config:
    # Basic Flask Config
    SECRET_KEY = os.environ.get('SECRET_KEY', 'placement-portal-2026-secret')
    
    # SQLAlchemy Config
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'ppa.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Config
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'placement-portal-app-2026-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_TOKEN_LOCATION = ['headers']
    ENV = os.environ.get("FLASK_ENV", "development")
    DEBUG = ENV == "development"

    # Mail (SMTP) Config - Set your credentials directly here
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'asmita.pal1010@gmail.com'  # sender email
    MAIL_PASSWORD = 'njzl fyli tzti idkt'  # app password
    MAIL_DEFAULT_SENDER = 'asmita.pal1010@gmail.com'  # username
    MAIL_SUPPRESS_SEND = False  # Set to True to disable sending 

    # Redis Cache Config
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 0
    CACHE_REDIS_URL = "redis://localhost:6379/0"
    CACHE_DEFAULT_TIMEOUT = 300

    # Celery Config
    CELERY_CONFIG = {

    # Redis connections
    "broker_url": "redis://localhost:6379/1",
    "result_backend": "redis://localhost:6379/2",
    "broker_connection_retry_on_startup": True,

    # timezone for scheduling
    "timezone": "Asia/Kolkata",


    # monthly scheduled task
    "beat_schedule": {
        "monthly-placement-report": {
            "task": "generate_monthly_report",

            # 9:00 AM on 1st day of every month
            "schedule": crontab(
                minute=0,
                hour=9,
                day_of_month=1
            ),
        },
    }
    }