# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))

if user_input == 0:
    user_choice = rock
    print(rock)
elif user_input == 1:
    user_choice = paper
    print(paper)
elif user_input == 2:
    user_choice = scissors
    print(scissors)

print('Computer chose:\n')
choice_list = [rock, paper, scissors]

computer_choice = random.choice(choice_list)

print(computer_choice)

if user_choice == computer_choice:
    print("It's a Draw!!")
else:
    if user_choice == rock and computer_choice == scissors:
        print('You have won!')
    elif user_choice == scissors and computer_choice == rock:
        print('You lose!')
    elif user_choice == scissors and computer_choice == paper:
        print('You have won!')
    elif user_choice == paper and computer_choice == scissors:
        print('You lose!')
    elif user_choice == paper and computer_choice == rock:
        print('You have won!')
    elif user_choice == rock and computer_choice == paper:
        print('You lose!')

