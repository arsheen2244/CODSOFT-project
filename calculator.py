# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.

# Perform the calculation and display the result
from tkinter import *
def add(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    if num2==0:
        return "Error!Division by Zero"
    else:
        return num1/num2
def exponent(num1,num2):
    return num1**num2
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
print("Welcome to Simple Calculator!")
print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponent")
n=int(input("CHOICE (1/2/3/4/5):"))
if n==1:
    print("Result ",add(num1,num2))
elif n==2:
    print("Result :",subtraction(num1,num2))
elif n==3:
    print("Result :",multiplication(num1,num2))
elif n==4:
    print("Result :", division(num1,num2))
elif n==5:
    print("Result :",exponent(num1,num2))
else:
    print("Invalid Input")



