# Write a program to print all even number that falls between two numbers (exclusive both numbers) entered from the user using while loop
def result():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    if a%2!=0:
     a+=1
    while(a<b-1):
        print(a)
        a=a+2

result()

