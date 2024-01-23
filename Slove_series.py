# Write a program in python to enter the number till the user wants and at the end it should display the sum of the number entered.

import os
ch='Y'
sum=0
while ch.upper()=='Y':
    num=int(input("Enter any number: "))
    sum=sum+num
    ch=input("DO you wish to continue(Y,N)?:")
    print(f"Sum of all the number is: {sum}")
