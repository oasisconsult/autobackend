class OnboardingFlow:

    def get_next_step(self, user_state: dict):

        if not user_state.get("project_created"):
            return "CREATE_FIRST_PROJECT"

        if not user_state.get("generation_run"):
            return "RUN_FIRST_GENERATION"

        return "ACTIVATED"