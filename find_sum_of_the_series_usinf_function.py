# Write a program to find the sum of the following series(accept values of X and N from user) 
# 1+x/1! +x^2/2! + .........X^n/n!

import os
import math
def series():
    s=1.0
    for i in range(1,number+1):
        s=s+math.pow(X,i)/math.factorial(i)
        print(s)

number=int(input("Enter any number of terms: "))
X=int(input("Enter the base"))
series()
