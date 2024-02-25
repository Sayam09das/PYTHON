# Find the product of all elements in a tuple:
from functools import reduce

my_tuple = (1, 2, 3, 4, 5)
product = reduce(lambda x, y: x * y, my_tuple)
print("Product of elements:", product)
