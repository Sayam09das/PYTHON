# Write a program to find the product of the digit of a number accepted from the user
def result():
    num=int(input("Enter a number: "))
    product=1
    while num>0:
        digit=num%10
        product *=digit
        num //= 10  # Remove the last digit from the number
    print("The product of the digits is: ",product)

result()