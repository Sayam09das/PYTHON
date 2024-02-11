# Write a Python program to print this a^3 + 3a^2b + 3ab^2 + b^3

def result():
    a=int(input("Enter the value of a: "))
    b=int(input("Enter the value of b: "))
    c=(a**3) + (3*a**2*b) + (3*a*b**2) + (b**3)
    print(f"The value is:{c}")

result()