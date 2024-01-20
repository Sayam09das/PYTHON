# Write a python program to swap two number without 3rd veriable
a=int(input("Enter the 1st value: "))
b=int(input("Enter the 2nd value: "))
print(f"Before swapping the value is: {a} and {b}")
a=a+b
b=a-b
a=a-b
print(f"After  swaping the is: {a} and {b}")