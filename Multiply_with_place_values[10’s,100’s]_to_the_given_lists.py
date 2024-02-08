#  Multiply with place values[10’s,100’s] to the given lists

list1 = [[1, 2], [3, 4]]
m = 1
print("Original List:", list1)

for i in range(0, 2):
    m *= 10
    for j in range(0, 2):
        list1[i][j] *= m


print("Modified List:", list1)
