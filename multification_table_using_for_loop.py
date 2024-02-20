def multi():
    for i in range(1,11):
        multiplication =number*i  
        print(f"{number} x {i} = {multiplication}")

number = int(input("Enter any number: "))
multi()



# The range in the for loop, range(1, 11), is used to iterate from 1 to 10 (inclusive). This is because you typically want to print the multiplication table from 1 to 10. The range is specified as [start, stop), where start is inclusive and stop is exclusive.

# So, range(1, 11) includes the numbers 1, 2, 3, ..., 10. If you wanted to print the multiplication table up to a different number, you could adjust the range accordingly.

# For example, if you wanted to print the multiplication table up to 12, you would use range(1, 13):
