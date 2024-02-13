# Write a program to reverse the number a accepted from usr using while loop
def reverse():
    num = int(input("Enter any number: "))
    num2 = 0

    while num != 0:
     rev = num % 10
     num2 = num2 * 10 + rev
     num = num // 10

    print("Reverse number is:", num2)

reverse()
