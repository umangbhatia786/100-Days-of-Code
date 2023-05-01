from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

print(logo)
question_bank = list()

for entry in question_data:
    
    new_question = Question(entry['text'], entry['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{len(question_bank)}")