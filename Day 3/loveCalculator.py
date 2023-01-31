# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2
test_list = list(combined_string.lower().replace(' ', ''))


true_count_dict = {x:test_list.count(x) for x in test_list if x in ['t', 'r', 'u', 'e']}
love_count_dict = {x:test_list.count(x) for x in test_list if x in ['l','o','v','e']}


sum_true = 0
for k,v in true_count_dict.items():
    sum_true += v

sum_love = 0
for k,v in love_count_dict.items():
    sum_love += v

love_score = int(str(sum_true) + str(sum_love))

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score > 40 and love_score < 50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')
