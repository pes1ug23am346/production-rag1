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

# =========================
# TITLE
# =========================

st.title("🤖 Production RAG Assistant")

st.markdown("""
Ask questions over research papers using:

- Hybrid Retrieval (BM25 + FAISS)
- Cross-Encoder Reranking
- Citation-Based Responses
- Hugging Face + LangChain
""")

# =========================
# METRICS
# =========================

col1, col2, col3 = st.columns(3)

col1.metric("Documents", "3 PDFs")
col2.metric("Retriever", "BM25 + FAISS")
col3.metric("Tests", "2/2 Passed")

# =========================
# SIDEBAR
# =========================

st.sidebar.header("Project Info")

st.sidebar.success("Hybrid Retrieval")
st.sidebar.success("Cross Encoder Reranking")
st.sidebar.success("Citation-Based Answers")
st.sidebar.success("GitHub Actions CI")

# =========================
# QUESTION INPUT
# =========================

question = st.text_area(
    "Ask a question about the documents",
    height=120,
    placeholder="Example: What is Retrieval Augmented Generation?"
)

# =========================
# SEARCH BUTTON
# =========================

if st.button("🔍 Search", use_container_width=True):

    if question:

        with st.spinner("Searching knowledge base..."):

            answer = ask_docs(question)

        st.divider()

        st.subheader("📄 Answer")

        st.info(answer)

# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "Built using FAISS, BM25, Cross-Encoder Reranking, Hugging Face, LangChain and Streamlit"
)
