import re

def extract_numbers(text):
    return set(re.findall(r"\b\d+\.?\d*\b", text))

def fact_precision_recall(llm_text, ground_truth):
    llm_nums = extract_numbers(llm_text)
    gt_nums = extract_numbers(ground_truth)

    true_positive = len(llm_nums & gt_nums)
    precision = true_positive / (len(llm_nums) + 1e-6)
    recall = true_positive / (len(gt_nums) + 1e-6)

    return round(precision, 2), round(recall, 2)
