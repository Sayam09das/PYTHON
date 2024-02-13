# Write a program in python to check in python by while loop
def prime():
    num = int(input("Enter any number: "))
    if num > 1:
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                print(f"This number is not a prime number")
                break
            divisor += 1
        else:
            print(f"This number is a prime number")
    else:
        print(f"This number is not a prime number")

prime()
