# Write a program in python to enter the number till the user wants and at the end it should display the sum of the number entered.

def series():
    sum = 0
    while True:
        num = int(input("Enter any number: "))
        sum += num
        ch = input("Do you wish to continue (Y/N)?: ")
        if ch.upper() != 'Y':
            break
    print(f"Sum of all the numbers is: {sum}")

series()
