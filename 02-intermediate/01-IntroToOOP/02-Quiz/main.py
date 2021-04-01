from question_model import Question
from data import question_data
from data_trivia import question_trivia
from quiz_brain import QuizBrain

question_bank = []

# using data
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

# using data_trivia
for question in question_trivia:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
# print(help(QuizBrain))

while quiz.still_has_questions():
    quiz.next_question()
print("End of Quiz")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
