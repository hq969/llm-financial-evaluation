def final_risk_score(precision, recall, hallucination, regulatory):
    score = (
        (1 - hallucination) * 0.4 +
        precision * 0.3 +
        recall * 0.2 +
        (1 - regulatory) * 0.1
    )
    return round(score, 2)
