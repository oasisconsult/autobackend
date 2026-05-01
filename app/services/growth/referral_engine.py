import uuid


class ReferralEngine:

    def generate_referral_code(self, user_id: str):

        return f"ref_{user_id[:6]}_{uuid.uuid4().hex[:6]}"

    def reward_referral(self, db, referrer_id: str):

        # simple credit system
        return {
            "credits_added": 10,
            "message": "Referral reward granted"
        }