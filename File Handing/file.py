f = open("G:\\html\\my_Web_page\\python\\File Handing\\file.txt", "r") #Complete parth or only use txt file 
file_read = f.read()
print(file_read)  
print(type(file_read))

# How to close the file 
f.close() # please comment out
