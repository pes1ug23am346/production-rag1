from langchain_text_splitters import RecursiveCharacterTextSplitter

from ingest import load_documents


def chunk_documents():
    docs = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = splitter.split_documents(docs)

    return chunks


if __name__ == "__main__":
    chunks = chunk_documents()

    print(f"Created {len(chunks)} chunks")

    print("\nFirst Chunk Metadata:")
    print(chunks[0].metadata)

    print("\nFirst Chunk Preview:")
    print(chunks[0].page_content[:500])

