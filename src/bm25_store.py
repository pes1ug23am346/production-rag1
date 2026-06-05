from rank_bm25 import BM25Okapi

from chunker import chunk_documents


def create_bm25():
    chunks = chunk_documents()

    tokenized_docs = [
        chunk.page_content.lower().split()
        for chunk in chunks
    ]

    bm25 = BM25Okapi(tokenized_docs)

    return bm25, chunks


if __name__ == "__main__":
    bm25, chunks = create_bm25()

    query = "What is Retrieval Augmented Generation?"

    tokenized_query = query.lower().split()

    scores = bm25.get_scores(tokenized_query)

    top_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:3]

    print(f"\nQuery: {query}\n")

    for rank, idx in enumerate(top_indices, start=1):
        print("=" * 50)
        print(f"Result {rank}")
        print(chunks[idx].metadata)
        print(chunks[idx].page_content[:500])
        print()
