from fastapi import APIRouter, Depends

from app.core.security import get_current_user
from app.services.growth.referral_engine import ReferralEngine

router = APIRouter()


@router.get("/code")
def get_code(user=Depends(get_current_user)):

    engine = ReferralEngine()

    return {
        "code": engine.generate_referral_code(user["sub"])
    }