class ActivationEngine:

    def check_activation(self, user_events: list):

        has_created_project = any(
            e["type"] == "project_created"
            for e in user_events
        )

        has_run_generation = any(
            e["type"] == "generation_success"
            for e in user_events
        )

        return has_created_project and has_run_generation