import textstat

PROHIBITED_PHRASES = [
    "buy now", "strong buy", "guaranteed returns",
    "you should invest", "best investment"
]

def regulatory_risk(llm_text):
    violations = [p for p in PROHIBITED_PHRASES if p in llm_text.lower()]
    risk_score = len(violations) / len(PROHIBITED_PHRASES)
    return round(risk_score, 2)

def readability_score(llm_text):
    return round(textstat.flesch_reading_ease(llm_text), 2)
