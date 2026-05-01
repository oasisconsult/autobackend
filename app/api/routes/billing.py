from fastapi import APIRouter, Depends
from app.api.deps import get_current_user

router = APIRouter()


USAGE = {}


@router.get("/usage")
def get_usage(user=Depends(get_current_user)):

    uid = user["sub"]

    return {
        "user_id": uid,
        "tokens_used": USAGE.get(uid, 0)
    }


@router.post("/track")
def track_usage(payload: dict, user=Depends(get_current_user)):

    uid = user["sub"]
    USAGE[uid] = USAGE.get(uid, 0) + payload.get("tokens", 0)

    return {"status": "ok"}


from fastapi import APIRouter
from app.services.stripe.checkout_service import CheckoutService

router = APIRouter()
service = CheckoutService()


@router.post("/checkout")
def create_checkout(payload: dict):

    url = service.create_checkout(
        tenant_id=payload["tenant_id"],
        email=payload["email"],
        price_id=payload["price_id"]
    )

    return {"checkout_url": url}