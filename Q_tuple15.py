# Merge two tuples and remove duplicates:
tuple1 = (1, 2, 3)
tuple2 = (3, 4, 5)
merged_tuple = tuple(set(tuple1 + tuple2))
print(merged_tuple)
