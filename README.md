# 🤖 Production RAG Assistant

A Retrieval-Augmented Generation (RAG) system that answers questions from research papers using Hybrid Search, Cross-Encoder Reranking, and LLM-based response generation.

## 🚀 Features

- Hybrid Retrieval (BM25 + FAISS)
- Cross-Encoder Reranking
- Citation-Based Answers
- Research Paper Question Answering
- Streamlit Web Interface
- Automated Testing with Pytest
- GitHub Actions CI Pipeline

---

## 🏗️ Architecture

User Question

↓


Hybrid Retrieval

(BM25 + FAISS)

↓

Cross Encoder Reranking

↓

Context Building

↓

LLM Generation

↓

Citation-Based Answer

↓

Streamlit UI

---

## 🛠️ Tech Stack

- Python
- LangChain
- FAISS
- Rank-BM25
- Hugging Face Embeddings
- Cross Encoder Reranker
- Streamlit
- Pytest
- GitHub Actions

---

## 📂 Project Structure

text production-rag1/ │ ├── data/ │   └── docs/ │ ├── faiss_index/ │ ├── src/ │   ├── chunker.py │   ├── vector_store.py │   ├── retriever.py │   ├── reranker.py │   ├── rag_chain.py │   └── evaluator.py │ ├── tests/ │   └── test_rag.py │ ├── app.py ├── requirements.txt └── README.md 

## ⚙️ Installation

bash git clone https://github.com/pes1ug23am346/production-rag1.git  cd production-rag1  python -m venv venv  source venv/bin/activate  pip install -r requirements.txt 

## ▶️ Run Application

bash streamlit run app.py 

Open:

text http://localhost:8501 

## 🧪 Run Tests

bash pytest tests/test_rag.py -v 

## 💬 Sample Questions

- What is Retrieval Augmented Generation?
- How does RAG combine parametric and non-parametric memory?
- What are the advantages of Retrieval Augmented Generation?
- How does Cross-Encoder Reranking improve retrieval quality?

## ✅ Current Status

- PDF Ingestion Completed
- Hybrid Retrieval Implemented
- Cross Encoder Reranking Implemented
- Citation-Based Responses Implemented
- Streamlit UI Implemented
- Automated Tests Added
- GitHub Actions CI Enabled

## 🔮 Future Improvements

- Multi-document Upload
- Conversational Memory
- Docker Deployment
- Cloud Deployment
- Advanced Evaluation Metrics

## 👨‍💻 Author

Veerendra R Lashkare

PES University – CSE (AI & ML)
