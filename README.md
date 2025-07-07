# Briq-Background

A ready-to-use Docker Compose setup for running Redis, Celery (with Beat for cron jobs), and Flower for remote background task management and monitoring.

---

## Features

- **Redis**: Message broker and result backend for Celery.
- **Celery**: Runs worker and Beat for scheduled (cron) jobs.
- **Flower**: Web UI for monitoring Celery tasks and workers.

---

## Quick Start

### 1. Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop) and [Docker Compose](https://docs.docker.com/compose/) installed.
- (Recommended) Basic Linux server security (firewall, strong passwords).

### 2. Clone and Configure

```sh
git clone <this-repo-url>
cd briqBackground
```

Create a `.env` file with strong credentials:

```
REDIS_PASSWORD=your_secure_redis_password
FLOWER_USER=admin
FLOWER_PASSWORD=your_secure_flower_password
```

### 3. Build and Start Services

```sh
docker-compose up -d --build
```

- **Redis** will be available on port `6379` (secured with your password).
- **Flower** dashboard will be at [http://<your-server-ip>:5555](http://<your-server-ip>:5555) (login with your Flower credentials).

### 4. Secure Your Server

- Restrict access to Redis and Flower ports using your firewall (e.g., UFW):

  ```sh
  sudo ufw allow from <your-app-server-ip> to any port 6379
  sudo ufw allow from <your-ip> to any port 5555
  sudo ufw deny 6379
  sudo ufw deny 5555
  ```

- (Optional) Set up HTTPS for Flower using a reverse proxy like Nginx.

---

## Using with Your External Application

- **Celery/Redis Connection String** (from your app server):

  ```
  redis://:your_secure_redis_password@<your-server-ip>:6379/0
  ```

- **Celery Example**:

  ```python
  from celery import Celery
  app = Celery('your_app',
      broker='redis://:your_secure_redis_password@<your-server-ip>:6379/0',
      backend='redis://:your_secure_redis_password@<your-server-ip>:6379/0'
  )
  ```

- **Scheduled Tasks (Cron Jobs)**:  
  The included `celery.py` defines a periodic task (`process_scheduled_messages_task`) that runs every 5 minutes.  
  - If this task is defined in your external app, it will be picked up and executed by the worker.
  - If you want to schedule other tasks, edit the `beat_schedule` in `celery.py`.

---

## Customization

- **Add More Scheduled Tasks**:  
  Edit `celery.py` and update the `beat_schedule` dictionary.
- **Change Ports**:  
  Edit `docker-compose.yml` as needed.
- **Update Dependencies**:  
  Edit `requirements.txt` and rebuild.

---

## Stopping Services

```sh
docker-compose down
```

---

## Troubleshooting

- **Celery/Beat errors**: Ensure your external app defines the scheduled tasks, and the task names match.
- **Connection issues**: Check firewall rules and that your `.env` passwords are correct.
- **Redis memory warning**: On the server, run:
  ```sh
  sudo sysctl vm.overcommit_memory=1
  echo "vm.overcommit_memory = 1" | sudo tee -a /etc/sysctl.conf
  ```

---

## References

- [Celery Documentation](https://docs.celeryq.dev/en/stable/)
- [Flower Documentation](https://flower.readthedocs.io/en/stable/)
- [Redis Security](https://redis.io/docs/management/security/)

---

Made with heart from briq 💖
