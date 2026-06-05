import os

from dotenv import load_dotenv
from openai import OpenAI

from reranker import rerank

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)

MODEL_NAME = "openai/gpt-oss-20b"


def build_context(ranked_docs):
    context = ""

    for _, doc in ranked_docs:
        context += f"\n\nSOURCE: {doc.metadata['source_file']}"
        context += f"\nPAGE: {doc.metadata['page']}"
        context += f"\nCONTENT:\n{doc.page_content}"

    return context


def ask_docs(question):
    ranked_docs = rerank(question)

    context = build_context(ranked_docs)

    prompt = f"""
You are a document QA assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
reply exactly:

I don't know based on the provided documents.

Always include citations.

Citation format:
[SOURCE: filename.pdf | PAGE: x]

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=500
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    question = input("Ask a question: ")

    answer = ask_docs(question)

    print("\nAnswer:\n")
    print(answer)

