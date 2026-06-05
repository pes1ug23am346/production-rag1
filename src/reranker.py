from sentence_transformers import CrossEncoder

from retriever import hybrid_search


MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"


def rerank(query, top_k=5):
    docs = hybrid_search(query, k=20)

    model = CrossEncoder(MODEL_NAME)

    pairs = [
        (query, doc.page_content)
        for doc in docs
    ]

    scores = model.predict(pairs)

    ranked = sorted(
        zip(scores, docs),
        key=lambda x: x[0],
        reverse=True
    )

    return ranked[:top_k]


if __name__ == "__main__":
    query = "What is Retrieval Augmented Generation?"

    results = rerank(query)

    print(f"\nQuery: {query}\n")

    for rank, (score, doc) in enumerate(results, start=1):
        print("=" * 60)
        print(f"Rank: {rank}")
        print(f"Score: {score:.4f}")
        print(doc.metadata)
        print(doc.page_content[:300])
        print()
