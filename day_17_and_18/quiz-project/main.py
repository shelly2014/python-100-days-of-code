from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import sys

logo = """
  ___        _                 _   _____    _       _       
 / _ \      (_)               | | |_   _|  (_)     (_)      
/ /_\ \_ __  _ _ __ ___   __ _| |   | |_ __ ___   ___  __ _ 
|  _  | '_ \| | '_ ` _ \ / _` | |   | | '__| \ \ / / |/ _` |
| | | | | | | | | | | | | (_| | |   | | |  | |\ V /| | (_| |
\_| |_/_| |_|_|_| |_| |_|\__,_|_|   \_/_|  |_| \_/ |_|\__,_|                                                                                              
"""
print(logo)
print("Welcome to Animal Trivia!")
print("""
Get ready for a wild adventure! 
You'll be challenged with 10 True/False questions. Each question will have a time limit of 10 seconds.
""")
choice = input("Are you ready? (Y/N): ").lower()
if choice != "y":
    print("See you next time!")

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

sys.exit()
