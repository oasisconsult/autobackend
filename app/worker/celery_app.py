from celery import Celery
from app.core.config import settings

celery = Celery(
    "autobackend",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    task_track_started=True,
    task_acks_late=True,   # IMPORTANT ensures tasks are re-queued if a worker crashes
    task_reject_on_worker_lost=True,  # Optional but recommended
    task_time_limit=300,  # Optional: set a time limit for tasks
    worker_prefetch_multiplier=1
)

