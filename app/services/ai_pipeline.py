from app.ai.agents.architect import run_architect
from app.ai.agents.critic import run_critic
from app.ai.agents.repair import run_repair
from app.services.runtime_validator import validate_runtime



import structlog

log = structlog.get_logger()



from app.services.billing_tracker import BillingTracker

# billing = BillingTracker()


# def run_pipeline(prompt: str, db, user_id, tenant_id):

#     result = ...

#     tokens_used = len(prompt.split()) * 2  # estimate

#     billing.track_generation(
#         db,
#         user_id=user_id,
#         tenant_id=tenant_id,
#         tokens=tokens_used
#     )

#     return result


from app.ai.healing.self_healing_engine import SelfHealingEngine


healer = SelfHealingEngine()


# def run_pipeline(prompt: str):

#     def generator(p):
#         return run_architect(p)  # your existing AI step

#     result = healer.run(prompt, generator)

#     return result


from app.ai.prompts.prompt_optimizer import PromptOptimizer

optimizer = PromptOptimizer()


def run_pipeline(prompt: str, prompt_name="default"):

    result = execute_ai_pipeline(prompt)

    optimization = optimizer.process_result(
        prompt_name,
        prompt,
        result
    )

    result["prompt_optimization"] = optimization

    return result



# def run_pipeline(prompt: str, db, user_id, tenant_id):
#     """
#     Core 3-step AI pipeline:
#     1. Architect builds system
#     2. Critic evaluates
#     3. Repair fixes issues
#     4. Runtime validation ensures it works
#     """

#     design = run_architect(prompt)
#     critique = run_critic(design)

#     # auto-repair loop (bounded)
#     max_iterations = 2
#     for _ in range(max_iterations):
#         if "FAIL" not in critique:
#             break
#         design = run_repair(design, critique)
#         critique = run_critic(design)

#     valid, runtime_msg = validate_runtime("./generated_app")

#     score = compute_score(critique, valid)

#     return {
#         "design": design,
#         "critique": critique,
#         "runtime_valid": valid,
#         "runtime_msg": runtime_msg,
#         "score": score
#     }


def compute_score(critique: str, valid: bool) -> int:
    if not valid:
        return 50
    if "MAJOR" in critique:
        return 70
    if "MINOR" in critique:
        return 85
    return 95
