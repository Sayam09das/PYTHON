# Write a python program to print sum of n numbers 
m=int(input("Enter the value of m: "))
n=int(input("Enter the value of n: "))
sum=0
while m<=n:
    sum=sum+m
    m=m+1
print(f"Sum is:{sum}")