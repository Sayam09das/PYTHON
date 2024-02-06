# Write a program to print numbers from 1 to 21 except multiple of 2 & 3.

# number=int(input("Enter any number: "))
for number in range(1,21):
    if number%2!=0 and number%3!=0:
        print(number)