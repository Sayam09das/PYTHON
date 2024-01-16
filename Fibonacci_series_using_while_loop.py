# Write a program in python to print Fibonacci series

num=int(input("Enter the number of terms: "))
first,second=0,1
i=0
print("Fibonacci series:",end=" ")
while i<num:
    print(first, end=", ")
    next=first+second
    first=second
    second=next
    i+=1