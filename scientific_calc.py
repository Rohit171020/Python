# import math
# def square_root(num):
#     return math.sqrt(num)
# def pow(base,exp):
#     return math.pow(base,exp)
# def factorial(num):
#     return math.factorial(num)
# def sin(deg):
#     return math.sin(math.radians(deg))

import random

quiz = [
    { 
        "question": "What is the capital of India?",
        "options": {
            "A": "Mumbai",
            "B": "Chennai",
            "C": "New Delhi",
            "D": "Kolkata"
        },
        "answer": "C"
    },
    {
        "question": "Who developed Python?",
        "options": {
            "A": "Guido van Rossum",
            "B": "Elon Musk",
            "C": "Bill Gates",
            "D": "Mark Zuckerberg"
        },
        "answer": "A"
    }
]


selected_question = random.choice(quiz)
print(selected_question["question"])
print()
for key, value in selected_question["options"].items():
    print(f"{key}: {value}")
user_answer = input("\nEnter your option (A/B/C/D): ").upper()
if user_answer == selected_question["answer"]:
    print("Correct!")
else:
    correct_option = selected_question["answer"]
    print("Wrong answer!")
    print(f"The correct answer is option {correct_option}: {selected_question['options'][correct_option]}")
