# Write a program to read the numbers until -1 is encountered. Also count the negative, positive, and Zeros entered by the user
negative = 0
positive = 0
zeros = 0
print("Enter -1 to exit.")
num = int(input("Enter any number: "))
while num != -1:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zeros += 1    
    num = int(input("Enter any number: ")) 
print(f"Count of positive numbers:{positive}")
print(f"Count of negative numbers:{negative}")
print(f"Count of zeros:{zeros}")

