from fastapi import APIRouter
from app.worker.tasks import generate_backend

router = APIRouter()

from fastapi import APIRouter, Depends
from app.api.deps import get_current_user
from app.worker.tasks import generate_backend

from app.core.rate_limit import limiter
from fastapi import Request


@router.post("/")
def generate_backend_api(payload: dict, user=Depends(get_current_user)):

    task = generate_backend.delay(
        prompt=payload["prompt"]
    )

    return {
        "task_id": task.id,
        "status": "processing"
    }

# @router.post("/")
# def generate(payload: dict):

@router.post("/")
@limiter.limit("3/minute")
def generate(request: Request, payload: dict, user=Depends(get_current_user)):
    task = generate_backend.delay(payload["prompt"])

    return {
        "task_id": task.id,
        "status": "processing"
    }
    
from celery.result import AsyncResult

from celery.result import AsyncResult


@router.get("/{task_id}")
def get_generation_status(task_id: str, user=Depends(get_current_user)):

    task = AsyncResult(task_id)

    return {
        "status": task.status,
        "result": task.result if task.ready() else None
    }
    

# @router.get("/{task_id}")
# def status(task_id: str):

#     task = AsyncResult(task_id)

#     return {
#         "status": task.status,
#         "result": task.result if task.ready() else None
#     }
    
import subprocess
import requests
import time

def validate_runtime(path: str):

    build = subprocess.run(
        ["docker", "build", "-t", "gen", path],
        capture_output=True
    )

    if build.returncode != 0:
        return False, "build failed"

    run = subprocess.Popen(["docker", "run", "-p", "8001:8000", "gen"])

    time.sleep(5)

    try:
        r = requests.get("http://localhost:8001/health")
        return r.status_code == 200, "ok"
    except:
        return False, "failed"
    
from openai import OpenAI

client = OpenAI()

def call_llm(messages, model="gpt-5-mini"):
    res = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2
    )
    return res.choices[0].message.content


def check_limit(user_usage, limit=100):
    if user_usage > limit:
        raise Exception("Limit exceeded")