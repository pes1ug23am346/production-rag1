from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_documents(data_dir="data/docs"):
    documents = []

    for pdf_file in Path(data_dir).glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_file))
        docs = loader.load()

        for doc in docs:
            doc.metadata["source_file"] = pdf_file.name

        documents.extend(docs)

    return documents


if __name__ == "__main__":
    docs = load_documents()

    print(f"Loaded {len(docs)} pages")

    if docs:
        print("\nMetadata:")
        print(docs[0].metadata)

        print("\nContent Preview:")
        print(docs[0].page_content[:500])
