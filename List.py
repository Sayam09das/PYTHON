# List all operation:- 
list=[1,2,3,4,5,6,]
print(list)

# How to find length of a list .
print(len(list))

# How to add one singal value in list .     
a=[10,30,50,]
a.append(100)
print(a)

# How to add more value in list .
b=[30,50,79,45]
b.extend([10,20,90])
print(b)

# Q. Difference between append and extend ?


# Remove Particular element from particular index position.
c=[1,2,3,4,5,6,7,8,9]
c.pop(3)
print(c)
# output: [1, 2, 3, 5, 6, 7, 8, 9]  The index position 3. Mean 3 position value is 4 so 4 is remove .


# Remove Particular element from the list .
d=[1,2,3,4,5,6,7]
d.remove(5)
print(d)  
# output: [1, 2, 3, 4, 6, 7]  The value is 5 is remove .

#  Q. Difference between pop and remove ?
# ans:- pop mean:- Use the index position. 
#       remove mean:- Use the the only value.


# How to delete list index position.
e=[1,2,3,4,5,6,7]
del e[4]
print(e)

# How to delete list element.
f = [1, 2, 3, 4, 5, 6]
f.clear()
print(f)

# How to sorted list element.
list1=["c" , "a" , "d" ,"b"]
list2=sorted(list1)
print(list2)

#
list3=[10,20,50,110,60,80,110,70,110,90,110,30]
a=list3.count(110)
print(a)