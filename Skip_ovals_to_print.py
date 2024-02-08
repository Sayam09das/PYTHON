# Skip ovals to print from the sentence ‘Python Logic For Kids’

for i in 'python Logics For Kids':
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        continue
    print(i,end=" ")