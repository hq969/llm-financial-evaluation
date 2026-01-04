import pandas as pd
import streamlit as st

st.set_page_config(page_title="LLM Financial Evaluation", layout="wide")

st.title("LLM Financial Accuracy & Compliance Dashboard")

df = pd.read_csv("results.csv")

st.metric("Average Final Score", round(df["final_score"].mean(), 2))
st.metric("Avg Hallucination Score", round(df["hallucination_score"].mean(), 2))
st.metric("Avg Regulatory Risk", round(df["regulatory_risk"].mean(), 2))

st.dataframe(df)

st.bar_chart(df[["precision", "recall", "final_score"]])
