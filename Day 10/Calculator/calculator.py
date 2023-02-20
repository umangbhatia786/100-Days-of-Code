from art import *
import os

def add(n1, n2):
    '''Function to add 2 numbers'''
    return n1 + n2

def subtract(n1, n2):
    '''Function to subtract 2 numbers'''
    return n1 - n2

def multiply(n1, n2):
    '''Function to multiply 2 numbers'''
    return n1 * n2

def divide(n1, n2):
    '''Function to divide 2 numbers'''
    return n1/n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def claculator():
    print(calculator_text)
    print(calculator_logo)

    first_number = float(input('What is your first number?: '))

    print('List of available operations are below: ')

    for k in operations.keys():
        print(k)

    should_continue = True

    while should_continue:
        input_operation = input('Pick an operation: ')
        second_number = float(input("What's the next number?: "))

        calc_func = operations[input_operation]

        output_val = calc_func(first_number, second_number)

        print(f'{first_number} {input_operation} {second_number} = {output_val}')

        if input(f"Type 'y' to continue calculating with {output_val}, or type 'n' to start a new calculation: ") == 'y':
            first_number = output_val
        else:
            should_continue = False
            os.system('clear')
            claculator()

claculator()
            
