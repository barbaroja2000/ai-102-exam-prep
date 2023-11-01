

import json
import random

def load_json(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{filename} not found.")
        exit(1)

def get_category(categories):
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category['name']}")
    while True:
        try:
            choice = int(input("Select a category by number: ")) - 1
            return categories[choice]['name'], categories[choice]['text']
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid number.")

def get_random_samples(category_name, questions):
    filtered_questions = [q for q in questions if q['category'] == category_name]
    sample_count = min(len(filtered_questions), 3)
    return random.sample(filtered_questions, sample_count)


def render_prompt(categories, questions):
    category_name, category_text = get_category(categories)
    random_samples = get_random_samples(category_name, questions)
    header = (f"You are an exam tutor helping me to prepare for the Microsoft Azure AI-102 exam.\n"
              f"I want to specifically target this domain:\n{category_name}\n"
              f"The exam tests the following:\n{category_text}\n\n"
              f"EXAMPLE QUESTIONS FOR {category_name}\n{'_' * 12}\n")

    try:
        with open('output.txt', 'w') as file:
            file.write(header)
            for i, sample in enumerate(random_samples, 1):
                options_string = '\n'.join(sample['options'])
                question_block = (f"{sample['question']}\nOptions:\n"
                                  f"{options_string}\n{'-' * 9}\n")

                file.write(question_block)
            instruction = ("Come up with 10 questions to test my knowledge. "
                           "Ask each question in turn in an interactive style and wait for my answer before continuing. "
                           "If I get an answer wrong provide a concise explanation of the right answer")
            file.write(instruction)
        print("Prompt can be found at `output.txt`")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    categories = load_json('blob.json')
    questions = load_json('sample_questions.json')
    render_prompt(categories, questions)
