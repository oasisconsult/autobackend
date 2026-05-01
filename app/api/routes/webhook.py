from fastapi import APIRouter, Depends, Request
from app.db.session import get_db
from app.services.tenant_provisioning import TenantProvisioning
from app.core.config import settings

router = APIRouter()

# @router.post("/stripe")
# async def stripe_webhook(request: Request):

#     payload = await request.body()
#     sig = request.headers.get("stripe-signature")

#     try:
#         event = stripe.Webhook.construct_event(
#             payload,
#             sig,
#             settings.STRIPE_WEBHOOK_SECRET
#         )

#     except Exception:
#         return {"error": "invalid webhook"}

#     if event["type"] == "invoice.paid":
#         print("Payment confirmed")

#     return {"status": "ok"}


@router.post("/stripe/webhook")
async def stripe_webhook(event: dict, db=Depends(get_db)):

    if event["type"] == "checkout.session.completed":

        tenant_id = event["data"]["object"]["metadata"]["tenant_id"]

        provisioning = TenantProvisioning()
        provisioning.provision(db, tenant_id)

    return {"status": "ok"}