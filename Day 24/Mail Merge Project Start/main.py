#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def get_invited_names_list():
    name_list = []
    with open('Day 24/Mail Merge Project Start/Input/Names/invited_names.txt','r') as f:
        name_list = f.readlines()

    refined_name_list = []
    for name in name_list:
        refined_name = name.replace("\n", "")
        refined_name_list.append(refined_name)
    return refined_name_list

def get_letter_template():
    temp_letter = None
    with open('Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt', 'r') as temp_file:
        temp_letter = temp_file.read()

    return temp_letter

def generate_letter_for_name(name, letter_template):
    actual_letter_text = letter_template.replace("[name]", name)
    output_file_path = f'Day 24/Mail Merge Project Start/Output/ReadyToSend/invite_to_{name}.txt'
    with open(output_file_path, 'w') as output_file:
        output_file.write(actual_letter_text)


name_list = get_invited_names_list()
letter_temp = get_letter_template()

for name in name_list:
    generate_letter_for_name(name,letter_temp)



    

