import pandas as pd
from src.llm_generate import generate_financial_summary
from src.evaluator import evaluate

data = pd.read_csv("data/sec_filings.csv")

results = []

for _, row in data.iterrows():
    llm_output = generate_financial_summary(row["filing_text"])
    metrics = evaluate(llm_output, row["ground_truth_summary"])

    results.append({
        "company": row["company"],
        "llm_output": llm_output,
        **metrics
    })

df_results = pd.DataFrame(results)
df_results.to_csv("dashboard/results.csv", index=False)

print("LLM Evaluation Completed.")
