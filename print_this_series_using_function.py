# Write a program in python to print the series.
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *

def series():
    rows=5
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print(" ")
series()