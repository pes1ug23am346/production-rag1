from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from chunker import chunk_documents


EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def create_vector_store():
    chunks = chunk_documents()

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    vectorstore.save_local("faiss_index")

    return vectorstore


def load_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

if __name__ == "__main__":
    vectorstore = create_vector_store()

    query = "What is Retrieval Augmented Generation?"

    results = vectorstore.similarity_search(
        query,
        k=3
    )

    print(f"\nQuery: {query}\n")

    for i, doc in enumerate(results, start=1):
        print("=" * 50)
        print(f"Result {i}")
        print(doc.metadata)
        print(doc.page_content[:500])
        print()
