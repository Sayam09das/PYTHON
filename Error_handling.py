try:
    a=int(input("Enter a number: "))
    for i in range(0,11):
        print(f"{a} * {i} =",a*i)
        i+=1
        
except:
    print("Error is in your code")

