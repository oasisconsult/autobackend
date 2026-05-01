from fastapi import APIRouter, Depends

from app.api.deps import get_current_user

router = APIRouter()

@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return {
        "user_id": user["sub"],
        "tenant_id": user["tenant_id"]
    }