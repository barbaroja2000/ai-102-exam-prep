# Exam Preparation Tool

This utility script assists in preparing for any multiple choice style exam; eg 

* AWS Data Engineer Associate
* Azure AI Fundamentals

It will generate prompts suitable for ChatGPT to generate an interactive quiz.

![Interactive quiz](https://i.imgur.com/7mcyUxY.png)


Examples provided here are for Microsoft Azure AI-102 AI Engineer but the format will work for any.
Example output in `example_output.txt`

## Getting Started

### Prerequisites

- Python 3.x

### Input Files

Ensure you have the following JSON files in the same directory as your script:

1. `blob.json`: Contains categories related to the exam and sub cateogies, or areas to cover.
2. `sample_questions.json`: Contains sample questions for each category.

```json
// blob.json
[
    {
        "name": "Category Name",
        "text": "Description of the category."
    },
    ...
]

// sample_questions.json
[
    {
        "category": "Category Name",
        "question": "Sample question?",
        "options": ["Option 1", "Option 2", ...]
    },
    ...
]