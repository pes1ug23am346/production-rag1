import sys
import os

sys.path.append(os.path.abspath("src"))

from retriever import hybrid_search
from reranker import rerank


def test_retrieval_returns_documents():
    docs = hybrid_search(
        "What is Retrieval Augmented Generation?"
    )

    assert len(docs) > 0


def test_reranker_returns_documents():
    docs = rerank(
        "What is Retrieval Augmented Generation?"
    )

    assert len(docs) > 0
