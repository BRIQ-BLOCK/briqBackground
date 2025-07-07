FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["sh", "-c", "celery -A celery:celery_app worker --loglevel=info & celery -A celery:celery_app beat --loglevel=info"]