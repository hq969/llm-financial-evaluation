def hallucination_score(llm_text, ground_truth):
    llm_facts = llm_text.lower().split()
    gt_facts = ground_truth.lower().split()

    unsupported = [w for w in llm_facts if w not in gt_facts]
    score = len(unsupported) / (len(llm_facts) + 1e-6)

    return round(min(score, 1.0), 2)
