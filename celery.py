from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    'Briq Celery',
    broker='redis://:${REDIS_PASSWORD}@redis:6379/0',
    backend='redis://:${REDIS_PASSWORD}@redis:6379/0',
    broker_connection_retry_on_startup=True,
    include=[]  # Empty if tasks are defined externally
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    enable_utc=True,
    result_expires=300,
)

# Celery Beat schedule for cron jobs
celery_app.conf.beat_schedule = {
    'process-scheduled-messages': {
        'task': 'app.workers.message.process_scheduled_messages_task',
        'schedule': crontab(minute='*/5'),  # Refresh every 5 minutes
    },
}