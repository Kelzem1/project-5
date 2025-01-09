import random
import json

def load_question():
    with open('questions.json', 'r') as f:
        questions = json.load(f)["questions"]
        
    return questions

def get_random_question(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)
        
    random_questions = random.sample(questions, num_questions)
    return random_questions

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(str(i+1) + ".", option)
    
    number = int(input("Select the correct number:"))
    if number < 0 or number > len(question["options"]):
        print("Invalid choice, defaulting to wrong answer")
        return False
    
    correct = question["options"][number -1] == question["answer"]
    return correct
    
questions = load_question()
random_questions = get_random_question(questions, 2)

for question in random_questions:
    ask_question(question)
print(random_questions)