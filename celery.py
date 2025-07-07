from celery import Celery

app = Celery(
    'briqBackgroundTasks',
    broker='redis://:${REDIS_PASSWORD}@redis:6379/0',
    backend='redis://:${REDIS_PASSWORD}@redis:6379/0',
    include=[]
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)