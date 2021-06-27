from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# filling question_bank with question_data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# creating a quiz from QuizBrain and passing question bank as argument
quiz = QuizBrain(question_bank)
# creating the quiz UI passing quiz as argument (it is a QuizBrain object)
quiz_ui = QuizInterface(quiz)
