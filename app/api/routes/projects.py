from fastapi import APIRouter, Depends
from app.api.deps import get_current_user

router = APIRouter()

# TEMP in-memory (replace with DB later)
PROJECTS = []


@router.post("/")
def create_project(payload: dict, user=Depends(get_current_user)):

    project = {
        "id": len(PROJECTS) + 1,
        "user_id": user["sub"],
        "tenant_id": user["tenant_id"],
        "name": payload.get("name", "Untitled"),
        "prompt": payload.get("prompt")
    }

    PROJECTS.append(project)

    return project


@router.get("/")
def list_projects(user=Depends(get_current_user)):

    return [
        p for p in PROJECTS
        if p["user_id"] == user["sub"]
    ]