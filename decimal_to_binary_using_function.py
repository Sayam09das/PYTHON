# Write a program to convert Decimal to Binary
def decimal():
    num = int(input("Enter a positive number: "))
    p = 1
    binary_num = 0
    real_number=num

    while num > 0:
        rem = num % 2
        binary_num = binary_num + rem * p
        p = p * 10
        num = num // 2

    print(f"Binary number of {real_number} is {binary_num}")

decimal()
