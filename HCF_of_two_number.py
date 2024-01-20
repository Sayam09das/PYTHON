# Write a program to find the HCF of two numbers enterd from the user

import os
num1=int(input("Enter first number: "))
num2=int(input("Enter the second number: "))
number1=num1
number2=num2
while num2 !=0:
    temp=num2
    num2=num1%num2
    num1=temp

hcf=num1
print(f"The HCF of {number1} and {number2} is: {hcf}")
    