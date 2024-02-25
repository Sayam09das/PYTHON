# Remove an element from a tuple:
my_tuple = (1, 2, 3, 4, 5)
element_to_remove = 3
new_tuple = tuple(e for e in my_tuple if e != element_to_remove)
print(new_tuple)
