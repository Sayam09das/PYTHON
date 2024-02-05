# Write a program in python to print Factorial of a number.
number=int(input("Enter any number: "))
fact=1
for i in range(1,number+1):
    fact =fact*i
print("The factorial is:", fact)