import sys
import os


sys.path.append(os.path.abspath("src"))

from pathlib import Path

import streamlit as st
from rag_chain import ask_docs
from vector_store import create_vector_store

st.set_page_config(
    page_title="Production RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

# =========================
# TITLE
# =========================

st.title("🤖 Production RAG Assistant")

st.caption("Upload PDF documents and ask questions with citation-based answers.")
from pathlib import Path

st.sidebar.divider()
docs = sorted(Path("data/docs").glob("*.pdf"))

with st.sidebar.expander(f"📚 Uploaded Documents ({len(docs)})"):

    if docs:
        for doc in docs:
            st.write(f"📄 {doc.name}")
    else:
        st.caption("No documents uploaded.")

# =========================
# SIDEBAR
# =========================
st.sidebar.divider()
st.sidebar.subheader("📄 Upload PDF")

uploaded_files = st.sidebar.file_uploader(
    "Choose PDF(s)",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    save_dir = Path("data/docs")
    save_dir.mkdir(parents=True, exist_ok=True)

    for uploaded_file in uploaded_files:

        save_path = save_dir / uploaded_file.name

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    with st.spinner("Indexing documents..."):
        create_vector_store()

    st.sidebar.success(f"{len(uploaded_files)} PDF(s) indexed successfully!")

st.sidebar.header("⚡ Features")

st.sidebar.markdown("""
- 📚 Multi PDF Support
- 🔍 Hybrid Retrieval (BM25 + FAISS)
- 🎯 Cross-Encoder Reranking
- 📄 Citation-Based Answers
""")
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

