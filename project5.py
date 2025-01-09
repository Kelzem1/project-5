import random
import json

def load_question():
    with open('questions.json', 'r') as file:
        questions = json.load(file)