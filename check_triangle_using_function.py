import math
def triangle():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))

    c = math.sqrt(a**2 + b**2)

    if c == math.sqrt(a**2 + b**2):
      print("It is a right-angled triangle")
    else:
      print("It is not a right-angled triangle")

triangle()
