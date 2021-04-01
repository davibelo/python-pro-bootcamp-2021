class QuizBrain:
    """ This class can be used to manipulate a simple prompt Quiz

        q_list: list of Question objects
        score: score of questions answered correctly"""

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """Print next question and checks user answer"""
        current_question = self.question_list[self.question_number]
        user_answer = input(
            f"Q.{self.question_number+1}: {current_question.text} (True or False)?")
        bank_answer = current_question.answer
        self.check_answer(user_answer, bank_answer)
        self.question_number += 1

    def still_has_questions(self):
        """return if new questions exists on question list"""
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, b_answer):
        """Checks user answer and keep a score"""
        if u_answer == b_answer:
            self.score += 1
            print(
                f"Congratulation! Score: {self.score}/{len(self.question_list)}")
        else:
            print(
                f"Wrong answer Score: {self.score}/{len(self.question_list)}")
        print("\n")
