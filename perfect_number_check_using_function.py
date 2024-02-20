# Write a program to accept a number and check whether it is a perfect number or not.
# (Perfect number is a positive integer which is equal to the sum of its divisors like divisors of 6 are 1,2,3)
# and of divisiors is also 6, so 6 is perfect number)

def perfect_number(number):
    s = 0
    for i in range(1, number):
        if number % i == 0:
            s = s + i

    if number == s:
        print("NUMBER IS PERFECT")
    else:
        print("NUMBER IS NOT PERFECT")

number = int(input("Enter any number: "))
perfect_number(number)
