import random
import json
import time
from termcolor import colored, cprint

user_list = [
    
]

class User:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        
def create_user():
    userName = input("Enter your name: ")
    userRate = 0
    u1 = User(userName, userRate)
    user_list.append(u1)
    

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
    
    inp_text = colored("Select the correct number: ", "cyan")
    number = int(input(inp_text))
    if number < 0 or number > len(question["options"]):
        print("Invalid choice, defaulting to wrong answer")
        return False
    
    correct = question["options"][number -1] == question["answer"]
    return correct


#START
create_user()
questions = load_question()
total_questions = int(input(colored("Enter the number of questions: ", "cyan")))
random_questions = get_random_question(questions, total_questions)
correct = 0
start_time = time.time()

for question in random_questions:
    is_correct = ask_question(question)
    if is_correct:
        correct += 1
    print("-----------------------")
    
    
completed_time = time.time() - start_time
cprint("Sumary:", "light_green")
print("Total Questions: ", total_questions)
print("Correct Answers: ", correct)
print("Score: ", str(round((correct / total_questions) * 100, 2)) + "%")
print("Time: ", round(completed_time, 2), "seconds")