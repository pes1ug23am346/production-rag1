import sys
import os

sys.path.append(os.path.abspath("src"))

import streamlit as st
from rag_chain import ask_docs

st.set_page_config(
    page_title="Production RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Production RAG Assistant")

st.sidebar.header("Project Info")

st.sidebar.success("Hybrid Retrieval")
st.sidebar.success("Cross Encoder Reranking")
st.sidebar.success("Citation-Based Answers")
st.sidebar.success("GitHub Actions CI")

question = st.text_input(
    "Ask a question about the documents"
)

if st.button("Search"):

    if question:

        with st.spinner("Searching knowledge base..."):

            answer = ask_docs(question)

        st.markdown("## Answer")

        st.write(answer)
