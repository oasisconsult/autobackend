import stripe


class UpgradeEngine:

    def create_upgrade_session(self, customer_id: str, price_id: str):

        return stripe.checkout.Session.create(
            mode="subscription",
            customer=customer_id,
            line_items=[{"price": price_id, "quantity": 1}],
            success_url="https://app.yourdomain.com/success",
            cancel_url="https://app.yourdomain.com/cancel"
        )