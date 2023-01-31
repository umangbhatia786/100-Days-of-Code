# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == 'S':
    size_price = 15
    if add_pepperoni == 'Y':
        pepperoni_price = 2
    else:
        pepperoni_price = 0
    
elif size == 'M' or size == 'L':
    if size == 'M':
        size_price = 20
    else:
        size_price = 25

    if add_pepperoni == 'Y':
        pepperoni_price = 3
    else:
        pepperoni_price = 0

if extra_cheese == 'Y':
    cheese_price = 1
else:
    cheese_price = 0

total_bill = size_price + pepperoni_price + cheese_price

print(f'Your final bill is: ${total_bill}.')

