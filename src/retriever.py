from rank_bm25 import BM25Okapi
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from chunker import chunk_documents

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def hybrid_search(query, k=5):
    chunks = chunk_documents()

    tokenized_docs = [
        chunk.page_content.lower().split()
        for chunk in chunks
    ]

    bm25 = BM25Okapi(tokenized_docs)

    bm25_scores = bm25.get_scores(
        query.lower().split()
    )

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    vector_results = vectorstore.similarity_search(
        query,
        k=10
    )

    combined = []

    combined.extend(vector_results)

    bm25_top = sorted(
        range(len(bm25_scores)),
        key=lambda i: bm25_scores[i],
        reverse=True
    )[:10]

    for idx in bm25_top:
        combined.append(chunks[idx])

    unique_docs = []
    seen = set()

    for doc in combined:
        text = doc.page_content[:100]

        if text not in seen:
            unique_docs.append(doc)
            seen.add(text)

    return unique_docs[:k]


if __name__ == "__main__":
    query = "What is Retrieval Augmented Generation?"

    results = hybrid_search(query)

    print(f"\nQuery: {query}\n")

    for i, doc in enumerate(results, start=1):
        print("=" * 50)
        print(f"Result {i}")
        print(doc.metadata)
        print(doc.page_content[:300])
        print()
