def fraud_safe_cost_check(risk_score: int, estimated_cost: float):

    if risk_score > 70 and estimated_cost > 0.5:
        raise Exception("High-risk request blocked due to cost exposure")

    if risk_score > 50:
        return estimated_cost * 0.5  # reduce model usage / cap response

    return estimated_cost