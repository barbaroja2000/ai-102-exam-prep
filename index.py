import json
import random

def get_category():
    with open('blob.json') as f:
        categories = json.load(f)
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category['name']}")
    choice = int(input("Select a category by number: ")) - 1
    return categories[choice]['name'], categories[choice]['text']

def get_random_samples(category_name):
    with open('sample_questions.json') as f:
        questions = json.load(f)

    # Filter questions for the selected category
    filtered_questions = [q for q in questions if q['category'] == category_name]

    # Select up to 3 random questions from the filtered list
    sample_count = min(len(filtered_questions), 3)
    random_samples = random.sample(filtered_questions, sample_count)
    
    return random_samples

def render_prompt():
    category_name, category_text = get_category()
    random_samples = get_random_samples(category_name)
    header = """you are an exam tutor helping me to prepare for the microsoft azure ai-102 exam. 
I want to specifically target this domain:
{}
the exam tests the following.
{}

The format of the exam questions can be single choice, multiple choice, true/false or fill in the blanks
-------------
EXAMPLE QUESTIONS FOR {}

{}
""".format(category_name, category_text,category_name, '_' * 12)

    with open('output.txt', 'w') as file:
        file.write(header)
        for i, sample in enumerate(random_samples, 1):
            question_block = """{}
Options:

{}

---------

""".format(sample['question'], '\n'.join(sample['options']))
            file.write(question_block)

        instruction = "Come up with 10 questions to test my knowledge. Ask each question in turn in an interactive style and wait for my answer before continuing. If I get an answer wrong provide a consise explanation of the right answer"
        file.write(instruction)

if __name__ == "__main__":
    render_prompt()
