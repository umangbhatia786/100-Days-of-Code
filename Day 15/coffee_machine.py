from art import logo
from machine_data import MENU,resources


def print_report():
    for k, v in resources.items():
        if k == 'water':
            print(f'Water: {v}ml')
        elif k == 'milk':
            print(f'Milk: {v}ml')
        elif k == 'coffee':
            print(f'Coffee: {v}g')
        elif k == 'money':
            print(f'Money: ${v}')

def check_resources(user_choice):
    if user_choice == 'espresso':
        if MENU[user_choice]['ingredients']['water'] > resources['water']:
            print(f'Sorry there is not enough water for {user_choice}. Order something else!')
            return False
        if MENU[user_choice]['ingredients']['coffee'] > resources['coffee']:
            print(f'Sorry there is not enough milk for {user_choice}. Order something else!')
            return False
        return True
    
    else:
        if MENU[user_choice]['ingredients']['water'] > resources['water']:
            print(f'Sorry there is not enough water for {user_choice}. Order something else!')
            return False
        if MENU[user_choice]['ingredients']['milk'] > resources['milk']:
            print(f'Sorry there is not enough milk for {user_choice}. Order something else!')
            return False
        if MENU[user_choice]['ingredients']['coffee'] > resources['coffee']:
            print(f'Sorry there is not enough coffee for {user_choice}. Order something else!')
            return False
        return True
        
        
    
def process_coins(count_quarters, count_dimes, count_nickels, count_pennies):
    return count_quarters * 0.25 + count_dimes * 0.1 + count_nickels * 0.05 + count_pennies * 0.01

def is_transaction_valid(user_input,input_money):
    if input_money < MENU[user_input]['cost']:
        print('Sorry that is not enough money. Money Refunded!')
        return False
    elif input_money > MENU[user_input]['cost']:
        spare_money = input_money - MENU[user_input]['cost']
        print(f"Here is ${round(spare_money,2)} dollars in change.")
        return True
    else:
        return True

def update_resources(user_input):
    if user_input == 'espresso':
        resources['water'] -= MENU[user_input]['ingredients']['water']
        resources['coffee'] -= MENU[user_input]['ingredients']['coffee']
        resources['money'] += MENU[user_input]['cost']
    else:
        resources['water'] -= MENU[user_input]['ingredients']['water']
        resources['milk'] -= MENU[user_input]['ingredients']['milk']
        resources['coffee'] -= MENU[user_input]['ingredients']['coffee']
        resources['money'] += MENU[user_input]['cost']

def refill_coffee_machine():
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100

def coffee_vending_machine():
    print(logo)
    is_machine_on = True

    while is_machine_on:
        
        user_input = input('What would you like? (espresso/latte/cappuccino): ')

        if user_input == 'report':
            print_report()
        elif user_input in ['espresso','latte','cappuccino']:
            if check_resources(user_input):
                n_quarters = int(input('How many quarters: '))
                n_dimes = int(input('How many dimes: '))
                n_nickels = int(input('How many nickels: '))
                n_pennies =  int(input('How many pennies: '))

                user_money = process_coins(n_quarters,n_dimes,n_nickels,n_pennies)

                if is_transaction_valid(user_input,user_money):
                    print(f'Here is your {user_input}! Enjoy')
                    update_resources(user_input)

                else:
                    continue
            else:
                continue
        elif user_input == 'off':
            is_machine_on = False
        elif user_input == 'refill':
            username = input('Enter admin username: ')
            password = input('Enter admin password: ')

            if username == 'admin' and password == 'admin':
                refill_coffee_machine()
            else:
                print('Invalid Credentials! Access denied')

coffee_vending_machine()
            





