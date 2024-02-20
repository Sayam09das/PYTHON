# Write a program in python to print Factorial of a number.
def factorial():
    fact=1
    for i in range(1,number+1):
        fact =fact*i
    print("The factorial is:", fact)

number=int(input("Enter any number: "))
factorial()