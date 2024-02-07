# Write a program in python to print the series.
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *

rows=5
for i in range(rows,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print(" ")