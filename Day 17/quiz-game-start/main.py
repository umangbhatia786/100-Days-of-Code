from question_model import Question
from data import DataGenerator
from quiz_brain import QuizBrain
from art import logo

print(logo)

ques_count = int(input('How many questions do you want in your quiz? : '))
print("\n")
question_level = input('What is the level of quiz that you want? (easy/medium/hard) : ')
print("\n")

data_gen = DataGenerator(ques_count,question_level)
question_data = data_gen.generate_question_data_from_trivia()

question_bank = list()

for entry in question_data:
    
    new_question = Question(entry['text'], entry['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{len(question_bank)}")