##
# Calculator program
#
# Author: XCC
# Date: 11/11/2020


## Defi ne the functions to yuse in the calculator ##

def add(num1, num2):
    total = 0
    return total

def subtract(num1, num2):
    difference = 0
    return difference

## Code to start the calculation process ##


# Ask the user for what they want the two operands to be
firstNum = input("Enter the first number\n")

secondNum = input("Enter the second number\n")

# Ask the user for the operation they wish to use
operation = input("Enter the operation (+,-,/,*) \n")

## Code for the actual calculation ##

# Check to see what operation to do and do the right operation

if operation == "+":
    print("The answer is: " + firstNum + " " + operation + " " + secondNum + " = " + str(add(int(firstNum), int(secondNum))))
elif operation == "-":
    print("The answer is: " + firstNum + " " + operation + " " + secondNum + " = " + str(subtract(int(firstNum), int(secondNum))))


