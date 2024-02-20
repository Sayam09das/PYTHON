# Write a progaram to check wheather a number is palindrom or not 
def palindrom():
    num = int(input("Enter a number: "))
    real_number = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if real_number == rev:
        print(f"{real_number} is a palindrome number")
    else:
        print(f"{real_number} is not a palindrome number")

palindrom()
