
import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bid_dict = {}

print('Welcome to the secret aucton program.')
bidder_name = input('What is your name?: ')
bidder_val = int(input('What is your bid?: $'))

bid_dict[bidder_name] = bidder_val

to_continue = input("Are there any other bidders? type 'yes' or 'no' ")

while to_continue == 'yes':
    os.system('cls')
    next_bidder_name = input('What is your name?: ')
    next_bidder_val = int(input('What is your bid?: $'))

    bid_dict[next_bidder_name] = next_bidder_val

    to_continue = input("Are there any other bidders? type 'yes' or 'no' ")

    if to_continue == 'no':
        break

max_bid_val = max([val for val in bid_dict.values()])

max_bidder = None

for k, v in bid_dict.items():
    if v == max_bid_val:
        max_bidder = k

print(f'The winner is {max_bidder} with a bid of {max_bid_val}')
