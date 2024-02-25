# Convert a tuple of integers to a tuple of strings:Convert a tuple of integers to a tuple of strings:
tuple_of_integers = (1, 2, 3, 4, 5)
tuple_of_strings = tuple(str(e) for e in tuple_of_integers)
print(tuple_of_strings)
