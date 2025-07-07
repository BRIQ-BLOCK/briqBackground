# Briq-Background

Docker Compose setup for Celery, Redis, and Flower background task management.

## Services Overview

- **Redis**: Acts as the message broker and result backend for Celery. It queues tasks and stores results.
- **Celery**: Executes background tasks. This setup runs both the worker (processing tasks) and beat (scheduling periodic tasks).
- **Flower**: Provides a web-based monitoring tool for Celery tasks and workers.

## How It Works

1. **Celery** workers connect to **Redis** to fetch and execute tasks.
2. **Celery Beat** schedules periodic tasks and sends them to the queue in Redis.
3. **Flower** connects to Redis and Celery to provide a dashboard at [http://localhost:5555](http://localhost:5555) for monitoring tasks and workers.

## Deployment

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop) and [Docker Compose](https://docs.docker.com/compose/) installed.

### Installing Docker and Docker Compose

1. Follow the official [Docker Engine installation guide](https://docs.docker.com/engine/install/).
2. Install Docker Compose by following the [Compose plugin installation guide](https://docs.docker.com/compose/install/).
3. Verify installation:
   ```sh
   docker --version
   docker compose version
   ```

### Steps

1. Clone this repository and navigate to the project directory.
2. Start all services with:
   ```sh
   docker-compose up
   ```
3. Access Flower dashboard at [http://localhost:5555](http://localhost:5555).
4. Redis will be available on port `6177` for debugging or direct access.

> **Note:** This setup is designed to be used remotely, connecting to your application deployed on a different server. There is no need to mount your application code into the containers.

### Stopping Services

To stop all services, press `Ctrl+C` in the terminal or run:
```sh
docker-compose down
```

## Customization

- Update environment variables in `docker-compose.yml` as needed.
- If you need to connect to a different Redis or Celery instance, adjust the broker URLs accordingly.

---
This setup is ideal for remote background task management and monitoring with Celery, Redis, and Flower.

Made with heart from briq 💖
