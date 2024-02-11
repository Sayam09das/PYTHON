# Write a program to calculate area of a triangle

import math
def area():
    s=float(input("Enter semi perimeter: "))
    a=float(input("Enter length of side a: "))
    b=float(input("Enter length of side b: "))
    c=float(input("Enter length of side c:"))
    area= math.sqrt(s)*(s - a)*(s - b)*(s - c)
    print(f"The area of the Triangle is:{area}")

area()