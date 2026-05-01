import stripe
from app.core.config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class CheckoutService:

    def create_checkout(self, tenant_id: str, email: str, price_id: str):

        session = stripe.checkout.Session.create(
            mode="subscription",
            customer_email=email,
            line_items=[{
                "price": price_id,
                "quantity": 1
            }],
            metadata={
                "tenant_id": tenant_id
            },
            success_url="https://app.yourdomain.com/success",
            cancel_url="https://app.yourdomain.com/cancel"
        )

        return session.url