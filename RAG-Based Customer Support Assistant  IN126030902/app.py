import streamlit as st
from src.workflow import build_graph

app = build_graph()

st.title("RAG Customer Support Assistant")

query = st.text_input("Ask your question")

if st.button("Submit"):
    result = app.invoke({"query": query})
    st.write(result["answer"])