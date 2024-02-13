# Write a program in python slove this question (a+a/2)= ans and the ans is even or odd.

def equation():
    a=float(input("Enter any value:"))
    b=a+(a/5)
    if (b%2==0):
        print("even")
    else:
        print("odd")

equation()