# Write a program in python to print factorial of a number.

def result():
    num = int(input("Enter any number: "))
    fact = 1

    while num > 0:
        fact = fact * num
        num = num - 1

    print("The factorial is:", fact)

result()

