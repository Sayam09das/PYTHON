# Write a python program to display exam result
# num>80= A and num>60 to 80= B and num>50 to 60=C and num>35 to 50=D and num<35= fail

num=int(input("Enter the number: "))
if num>=80:
    print("A")
elif num>=60 and num<=80:
    print("B")
elif num>=50 and num<=60:
    print("C")
elif num>=35 and num<=50:
    print("D")
else:
    print("Fail")
