#  Print the * pattern using nested for loops

number=int(input("Enter value to print start: "))
for i in range(1,number+1):
    for j in range(i):
        print('*',end=' ')
    print()

for i in range(number-1,0,-1):
    for j in range(i):
        print('*',end=" ")
    print(' ')
