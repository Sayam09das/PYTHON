# Write a program to diplay all the numbers which are divible by 11 but not by 2 between 100 and 500.
def divisible():
    for i in range(100,500):
        if i%11==0 and i%2!=0:
            print(i,end=' ')

divisible()