from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    
    question_text = question["text"]
    question_answer = question["answer"]

    new_ques = Question(question_text, question_answer)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)

while quiz.questions_remain():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score} out of {quiz.question_number}")

















