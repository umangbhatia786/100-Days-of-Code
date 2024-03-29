import random
import os
from art import logo, vs
from game_data import data

def get_random_account():
    '''Return a random account from game data'''
    return random.choice(data)

def format_data(account):
    '''Format account into printable format: name, description and country'''
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess,a_followers,b_followers):
    '''Function to check if user guess is correct or not'''
    if (guess == 'a' and a_followers > b_followers) or (guess == 'b' and b_followers > a_followers):
        return True
    return False


def higher_lower_game():
    print(logo)
    score = 0
    game_should_continue = True

    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f'Compare A: {format_data(account_a)}')
        print(vs)

        
        print(f'Compare B: {format_data(account_b)}')

        user_guess = input("Who has more followers? Type 'a' or 'b': ")

        is_correct = check_answer(user_guess, account_a['follower_count'], account_b['follower_count'])
        
        os.system('clear')
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")

        else:
           game_should_continue = False
           print(f"You're wrong! Final score is: {score}.") 


higher_lower_game()