from src.fact_checker import fact_precision_recall
from src.hallucination import hallucination_score
from src.compliance import regulatory_risk, readability_score
from src.metrics import final_risk_score

def evaluate(llm_text, ground_truth):
    precision, recall = fact_precision_recall(llm_text, ground_truth)
    hallucination = hallucination_score(llm_text, ground_truth)
    regulatory = regulatory_risk(llm_text)
    readability = readability_score(llm_text)

    final_score = final_risk_score(
        precision, recall, hallucination, regulatory
    )

    return {
        "precision": precision,
        "recall": recall,
        "hallucination_score": hallucination,
        "regulatory_risk": regulatory,
        "readability": readability,
        "final_score": final_score
    }
