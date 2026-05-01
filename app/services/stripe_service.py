import stripe
from app.core.config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeService:

    def create_customer(self, email: str):
        return stripe.Customer.create(email=email)

    def create_subscription(self, customer_id: str, price_id: str):
        return stripe.Subscription.create(
            customer=customer_id,
            items=[{"price": price_id}]
        )

    def create_usage_invoice(self, customer_id: str, amount: float):
        return stripe.InvoiceItem.create(
            customer=customer_id,
            amount=int(amount * 100),
            currency="usd",
            description="AI Backend Usage"
        )

    def finalize_invoice(self, customer_id: str):
        invoice = stripe.Invoice.create(customer=customer_id)
        stripe.Invoice.finalize_invoice(invoice.id)
        stripe.Invoice.pay(invoice.id)
        return invoice