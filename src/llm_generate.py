from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(model="gpt-4", temperature=0)

def generate_financial_summary(text):
    prompt = f"""
    Summarize the following financial text accurately.
    Do not give investment advice.
    Use neutral tone.

    Text:
    {text}
    """
    response = llm([HumanMessage(content=prompt)])
    return response.content
