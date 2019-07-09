'''
Script to demonstrate how to use a function in Python3
'''

# Function 1 does some action
def my_first_function():
    print('\nIt worked!')

# Function 2 accepts a variable
def my_second_function(name):
    print('\nMy name is {}'.format(name))

# Function 3 accepts 2 variables and performs some math
def my_third_function(number1, number2):
    print("\nLet's do some math on {0} and {1}".format(number1, number2))
    print('Addition: ' + str(number1 + number2))
    print()

# Set up our variables
# The input() statement prompts a user for input
name = input("\nWhat is your name? ")
num1 = 4
num2 = 99

# Executing the functions
my_first_function()
my_second_function(name)
my_third_function(num1, num2)