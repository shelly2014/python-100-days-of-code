import threading
import time

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.timer_10s_expired = False
        self.timer = None
        self.user_input = ""

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def timeout(self):
        self.timer_10s_expired = True

    def timer_countdown(self):
        self.timer = threading.Timer(10, self.timeout)
        self.timer.start()

    def get_user_input(self):
        self.timer_10s_expired = True
        self.user_input = input(f"Your answer (True/False): ")
        self.timer_10s_expired = False
        if self.timer.is_alive():
            self.timer.cancel()

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.timer_10s_expired = False
        self.user_input = ""
        self.timer_countdown()
        print(f"Q.{self.question_number}: {current_question.text}")
        input_thread = threading.Thread(target=self.get_user_input)
        input_thread.start()
        input_thread.join(timeout=10)

        if self.timer_10s_expired:
            print("\nTime's up! Please hit 'Enter' to proceed to the next question.")
            while input_thread.is_alive():
                pass
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
        else:
            self.check_answer(self.user_input, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
