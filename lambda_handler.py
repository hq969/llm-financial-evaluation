from src.evaluator import evaluate

def lambda_handler(event, context):
    llm_text = event["llm_text"]
    ground_truth = event["ground_truth"]

    metrics = evaluate(llm_text, ground_truth)

    return {
        "statusCode": 200,
        "body": metrics
    }
