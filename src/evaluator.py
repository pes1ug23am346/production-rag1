from datasets import Dataset

from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
)

evaluation_data = {
    "question": [
        "What is Retrieval Augmented Generation?"
    ],
    "answer": [
        "Retrieval-Augmented Generation combines a language model with external retrieved knowledge."
    ],
    "contexts": [
        [
            "Retrieval-Augmented Generation combines parametric and non-parametric memory."
        ]
    ],
    "ground_truth": [
        "RAG combines parametric and non-parametric memory."
    ]
}

dataset = Dataset.from_dict(evaluation_data)

result = evaluate(
    dataset=dataset,
    metrics=[
        faithfulness,
        answer_relevancy
    ]
)

print(result)
