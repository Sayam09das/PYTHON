# Print Alphabets
# A
# B C
# D E F
# G H I J
# K L M N O

val=65
for i in range(0,5):
    for j in range(0,i+1):
        ch=chr(val)
        print(ch,end=" ")
        val=val+1
    print()