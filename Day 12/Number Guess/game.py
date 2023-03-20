import random
from art import logo

print(logo)
print('Welcome to the Number Guessing Game!')
print('I am thinking of number between 1 and 100')

level_required = True
while(level_required):
    level = input("Choose a difficulty level. Type 'easy' or 'hard' : ")

    if level not in ['easy', 'hard']:
        print("Inavlid input! You need to enter only 'easy' or 'hard'")
        continue
    else:
        level_required = False
        if level == 'easy':
            attempts = 8
        else:
            attempts = 5

random_choice = random.randrange(1,100)
print(random_choice)
while(attempts>0):
    user_guess = int(input('Make a guess: '))

    if user_guess > random_choice:
        attempts -=1
        print('Too High!')
        print('Guess Again!')
        print(f'you have {attempts} attempts remaining to guess the number')
        continue
    elif user_guess < random_choice:
        attempts -=1
        print('Too Low!')
        print('Guess Again!')
        print(f'you have {attempts} attempts remaining to guess the number')
        continue
    else:
        print('You win! You finally guessed it right')
        break

if attempts == 0:
    print(f'The number was {random_choice}')
    print("You couldn't guess it this time. You lose!")

