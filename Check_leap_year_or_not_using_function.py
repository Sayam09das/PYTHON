# Write a program to check wheather a number is leap year or not

def leap():
    year=int(input("Enter any year: "))
    if((year%4==0) and ((year%100!=0)) or (year%400==0)):
        print("Leap year")
    else:
        print("Not a Leap year")

leap()