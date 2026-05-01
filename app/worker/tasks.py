from app.worker.celery_app import celery
from app.services.ai_pipeline import run_pipeline
from app.services.zip_builder import build_zip
from app.db.session import SessionLocal
from celery.exceptions import MaxRetriesExceededError


@celery.task(bind=True, max_retries=3)
def generate_backend(self, prompt: str):

    db = SessionLocal()

    try:
        # 1. Run AI pipeline
        result = run_pipeline(prompt)

        # 2. Build downloadable artifact
        zip_path = build_zip("./generated_app")

        return {
            "result": result,
            "download": zip_path
        }

    except Exception as exc:
        try:
            raise self.retry(exc=exc, countdown=5 * (self.request.retries + 1))
        except MaxRetriesExceededError:
            return {
                "status": "failed",
                "reason": "max retries reached"
            }

    finally:
        db.close()