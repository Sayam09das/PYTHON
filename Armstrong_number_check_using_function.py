# Write a program to check whether a number is armstrong or not (153=1^3+5^3+3^3).

import math
def Armstrong():
    num=int(input("Enter an interger: "))
    n=0
    result=0
    originalnumber=num
    while originalnumber !=0:
        originalnumber =originalnumber//10
        n+=1

    originalnumber=num
    while originalnumber !=0:
        remainder=originalnumber%10
        result+=math.pow(remainder,n)
        originalnumber=originalnumber//10

    if result==num:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

Armstrong()