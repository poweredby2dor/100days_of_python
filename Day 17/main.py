"""
This module contains an exercise for 100 Days of Python
"""


from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]

    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)


print(question_bank) # print whole list
print(question_bank[0].answer) # selective print
