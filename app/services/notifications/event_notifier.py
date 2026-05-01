class EventNotifier:

    def send_email(self, email: str, message: str):
        print(f"EMAIL to {email}: {message}")

    def send_product_alert(self, user_id: str, event: str):

        if event == "FIRST_GENERATION_SUCCESS":
            return "Show onboarding success modal"