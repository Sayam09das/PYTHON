# Append using: 
list1=[1,2,3,4]
list1.append(19)
print("Using Append the list is now:  ",list1)

# clear using:
list2=[1,2,3,4]
list2.clear()
print("Using clear the list is now:  ",list2)

# copy using:
list3=[1,3,4,5,6]
copy=list3.copy()
copy.append(7)
print("Using copy the list is now:  ",copy)

# count using:
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_of_4 = list4.count(4)
print("Count of 4 in the list:", count_of_4)

# extend using:
list5 = [1, 2, 3, 4]   
list5.extend([5, 6, 7])
print("Using extend the list is now:  ", list5) 

# index using:
list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
index_4=list6.index(4)
print("Using index the list is now:  ", index_4)

# insert using:
list7=[1,2,3,4]
list7.insert(2,19)  
print("Using insert the list is now:  ", list7) 

# pop using:
list8=[1,2,3,4]
list8.pop()
print("Using pop the list is now:  ", list8)

# remove using:
list9=[1,2,3,4]
list9.remove(2)
print("Using remove the list is now:  ", list9)

# reverse using:
list10=[1,2,3,4]
list10.reverse()
print("Using reverse the list is now:  ", list10)

# sort using:
list11=[1,2,3,4]
list11.sort()
print("Using sort the list is now:  ", list11)

# len using:
list12=[1,2,3,4]
length=len(list12)
print("Using len the list is now:  ", length)

#....................................................................................................................#

# count using:
tuple1=(1,2,3,4)
tuple1.count(4)
print("Count of 4 in the tuple:", tuple1)

# index using:
tuple2=(1, 2, 3, 4)
index_2=tuple2.index(2)
print("Using index the tuple is now:  ", index_2)

#.....................................................................................................................#

# calculate the length of the string:
string1="Hello World"
length=len(string1)
print("The length of the string is:", length)

# calculate the number of words in the string:
string2="Hello World"
words=string2.split()
number_of_words=len(words)
print("The number of words in the string is:", number_of_words)

# calculate the number of characters in the string:
string3="Hello World"
characters=len(string3)
print("The number of characters in the string is:", characters)

# capitalize using:
string4="hello, and welcome to my progrmming world."
txt=string4.capitalize()
print("Using capitalize the string is now:  ", txt)

# upper using:
string5="hello, and welcome to my progrmming world."
txt1=string5.upper()
print("Using upper the string is now:  ", txt1)

# lower using:
string6="hello, and welcome to my progrmming world."
txt2=string6.lower()
print("Using lower the string is now:  ", txt2)

# casefold using:
string7="hello, and welcome to my progrmming world."
txt3=string7.casefold()
print("Using casefold the string is now:  ", txt3)

# center using:
string8="hello, and welcome to my progrmming world."
txt4=string8.center(50)
print("Using center the string is now:  ", txt4)

# count using:
string9="hello, and welcome to my progrmming world."
count=string9.count("o")
print("Using count the string is now:  ", count)

# find using:
string10="hello, and welcome to my progrmming world."
index = string10.find("o")
print("Using find the string is now:  ", index)

# count using:
string11="hello, and welcome to my progrmming world."
index2 = string11.index("o")
print("Using index the string is now:  ", index2)

# encode using:
string12="hello, and welcome to my progrmming world."
encoded=string12.encode()
print("Using encode the string is now:  ", encoded)

# endswith using:
string13="hello, and welcome to my progrmming world."
end=string13.endswith("world")
print("Using endswith the string is now:  ", end)

# expandtabs using:
string14="hello, and welcome to my progrmming world."
tab=string14.expandtabs(2)
print("Using expandtabs the string is now:  ", tab)

# format using:
string15="hello, and welcome to my progrmming world."
format=string15.format()
print("Using format the string is now:  ", format)

# format_map using:
string16="hello, and welcome to my progrmming world."
mapping = {"name": "Alice", "place": "Python"}
formatted_string = string16.format_map(mapping)
print("Using format_map the string is now:  ",formatted_string)

# isalnum using:
string17="hello, and welcome to my progrmming world."
alnum=string17.isalnum()
print("Using isalnum the string is now:  ", alnum)

# isalpha using:
string18="hello, and welcome to my progrmming world."
alpha=string18.isalpha()
print("Using isalpha the string is now:  ", alpha)

# isascii using:
string19="hello, and welcome to my progrmming world."
ascii=string19.isascii()
print("Using isascii the string is now:  ", ascii)

# isdecimal using:
string20="hello, and welcome to my progrmming world."
decimal=string20.isdecimal()
print("Using isdecimal the string is now:  ", decimal)

# isdigit using:
string21="124563"
digit=string21.isdigit()
print("Using isdigit the string is now:  ", digit)

# isidentifier using:
string22 = "hello, and welcome to my programming world."
identifier = string22.isidentifier()
print("Using isidentifier the string is a valid Python identifier:", identifier)

# islower using:
string23 = "hello, and welcome to my programming world."
lower = string23.islower()
print("Using islower the string is now:", lower)

# isnumeric using:
string24 = "1234"
numeric = string24.isnumeric()
print("Using isnumeric the string is now:", numeric)

# isprintable using:
string25 = "hello, and welcome to my programming world."
result = string25.isprintable()
print("Using isprintable the string is now:", result)

# isspace using:
string26 = "   "
space = string26.isspace()
print("Using isspace the string is now:", space)

# istitle using:
string27 = "Hello, and Welcome to my Programming World."
result2=string27.istitle()
print("Using istitle the string is now:", result2)

# isupper using:
string28 = "HELLO, AND WELCOME TO MY PROGRAMMING WORLD."
upper = string28.isupper()
print("Using isupper the string is now:", upper)

# join using:
string29 = "hello, and welcome to my programming world."
separator = " "
result3 = separator.join(string29)
print("Using join the string is now:", result3)

# istitle using:
string30 = "Hello, and Welcome to my Programming World."
result4 = string30.title()
print("Using title the string is now:", result4)

# ljust using:
string31 = "hello, and welcome to my programming world."
padded_string = string31.ljust(10)
print("Using ljust the string is now:", padded_string)

# lstrip using:
string32 = "   Hello, World!   "
stripped_string = string32.lstrip()
print("Using lstrip the string is now:", stripped_string)

# partition using:
string33 = "Hello World"
separator = ","
result5 = string33.partition(separator)

# replace using:
string34 = "Hello World"
result6 = string34.replace("World", "Python")
print("Using replace the string is now:", result6)

# rfind using:
string35 = "Hello World"
result7 = string35.rfind("o")
print("Using rfind the string is now:", result7)

# rindex using:
string36 = "Hello World"
result8 = string36.rindex("Hello")
print("Using rindex the string is now:", result8)

# rjust using:  
string37 = "Hello World"
result9 = string37.rjust(20)
print("Using rjust the string is now:", result9)

# rpartition using:
string38 = "Hello World"
result10=string38.rpartition(" ")
print("Using rpartition the string is now:", result10)

# splitlines using:
string39 = "Hello\nWorld"
result11=string39.splitlines()
print("Using splitlines the string is now:", result11)

# startswith using:
string40 = "Hello World"
result12=string40.startswith("Hello")
print("Using startswith the string is now:", result12)

# strip using:
string41 = "   Hello, World!   "
result13=string41.strip()
print("Using strip the string is now:", result13)

# swapcase using:
string42 = "Hello, World!"
result14=string42.swapcase()
print("Using swapcase the string is now:", result14)

# title using:
string43 = "hello, and welcome to my programming world."
result15=string43.title()
print("Using title the string is now:", result15)

# translate using:
string44 = "Hello, World!"
table = string44.maketrans("H", "J")
result16=string44.translate(table)
print("Using translate the string is now:", result16)

# zfill using:
string45 = "Hello, World!"
result17=string45.zfill(20)
print("Using zfill the string is now:", result17)

#....................................................................................................................#

# clear using:
dict1={"name":"Alice","age":25}
dict1.clear()
print("Using clear the dictionary is now:  ", dict1)

# copy using:
dict2={"name":"Alice","age":25}
dict3=dict2.copy()
print("Using copy the dictionary is now:  ", dict3)

# fromkeys using:
dict4={"name":"Alice","age":25}
keys=["name","age"]
dict5=dict.fromkeys(keys)
print("Using fromkeys the dictionary is now:  ", dict5)

# get using:
dict6={"name":"Alice","age":25}
age=dict6.get("age")
print("Using get the dictionary is now:  ", age)
country=dict6.get("country")
print("Using get the dictionary is now:  ", country)

# items using:
dict7={"name":"Alice","age":25}
items=dict7.items()
print("Using items the dictionary is now:  ", items)

# keys using:
dict8={"name":"Alice","age":25} 
keys=dict8.keys()
print("Using keys the dictionary is now:  ", keys)

# pop using:
dict9={"name":"Alice","age":25}
dict9.pop("age")
print("Using pop the dictionary is now:  ", dict9)

# popitem using:
dict10={"name":"Alice","age":25}
items=dict10.popitem()
print("Using popitem the dictionary is now:  ", items)

# setdefault using:
dict11={"name":"Alice","age":25}
age=dict11.setdefault("age")
print("Using setdefault the dictionary is now:  ", age)

# update using:
dict12={"name":"Alice","age":25}
age=dict12.update({"age":30})
print("Using update the dictionary is now:  ", dict12)

# values using:
dict13={"name":"Alice","age":25}
value=dict13.values()
value_list=list(value)
print("Using values the dictionary is now:  ", value_list)

#....................................................................................................................#

#  add using:
set1={1,2,3}
set1.add(4)
print("Using add the set is now:  ", set1)

# difference using:
set2={1,2,3,4}
set3={2, 3, 5, 6}
set_result1=set2.difference(set3)
print("Using difference the set is now:  ", set_result1)

# intersection using:
set4={1, 2, 3, 4}
set5={2, 3, 5, 6}
set_result2=set4.intersection(set5)
print("Using intersection the set is now:  ", set_result2)

# isdisjoint using:
set6={1, 2, 3, 4}
set7={5, 6, 7, 8}
set_result3=set6.isdisjoint(set7)
print("Using isdisjoint the set is now:  ", set_result3)

#  difference using:
set8={1, 2, 3, 4}
set9={5, 6, 7, 8}
set_result4=set8.symmetric_difference(set9)
print("Using symmetric_difference the set is now:  ", set_result4)

# update using:
set10={1, 2, 3, 4}
set11={5, 6, 7, 8}
set10.update(set11)
print("Using update the set is now:  ", set10)

# discard using:
set12={1, 2, 3, 4}
set12.discard(2)
print("Using discard the set is now:  ", set12)

# remove using:
set13={1, 2, 3, 4}
set13.remove(2)
print("Using remove the set is now:  ", set13)

# pop using:
set14={1, 2, 3, 4}
set14.pop()
print("Using pop the set is now:  ", set14)

# intersection_update using:
set15={1, 2, 3, 4}
set16={2, 3, 5, 6}
set_result5=set15.intersection_update(set16)
print("Using intersection_update the set is now:  ", set_result5)

# issubset using:
set17={1, 2, 3, 4}
set18={2, 3}
set_result6=set17.issubset(set18)
print("Using issubset the set is now:  ", set_result6)

# issuperset using:
set19={1, 2, 3, 4}
set20={2, 3}
set_result7=set19.issuperset(set20)
print("Using issuperset the set is now:  ", set_result7)

# symmetric_difference_update using:
set21 = {1, 2, 3, 4, 5}
set22 = {4, 5, 6, 7, 8}
set21.symmetric_difference_update(set22)
print("Using symmetric_difference_update the set is now:", set21)

# union using:
set23 = {1, 2, 3, 4, 5}
set24 = {4, 5, 6, 7, 8}
set_result8 = set23.union(set24)
print("Using union the set is now:", set_result8)
