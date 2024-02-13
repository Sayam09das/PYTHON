# Write a python program to print sum of n numbers.
def result():
    n = int(input("Enter the value of n: "))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(f"Sum is: {sum}")

result()
