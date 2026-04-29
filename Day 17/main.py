"""
This module contains an exercise for 100 Days of Python
"""

# Create a Question class with a __init()__ method with 2 attributes: text and answer attribute.


class Question:
    def __init__(self, q_text, q_answer):
        self.question = q_text
        self.answer = q_answer
        print("Question class has been created.")


new_q = Question("text", "answer")

print(new_q.question)
