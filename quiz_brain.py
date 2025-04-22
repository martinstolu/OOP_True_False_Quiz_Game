class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.list):
            return True
        else:
            print(f"You've completed the quiz\n"
                  f"Your final score was: {self.score}/{self.question_number}")
            return False



    def next_question(self):
        current_question = self.list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: "
                    f"{current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, list_answer):
        if user_answer.lower() == list_answer.lower():
            print("correct")
            self.score += 1
        else:
            print(f"wrong, the answer : {list_answer}")
        print(f"Your current score is:"
              f" {self.score}/{self.question_number}")
        print("\n")