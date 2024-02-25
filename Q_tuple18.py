# Count the number of even and odd numbers in a tuple:
my_tuple = (1, 2, 3, 4, 5)
even_count = sum(1 for e in my_tuple if e % 2 == 0)
odd_count = sum(1 for e in my_tuple if e % 2 != 0)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
    