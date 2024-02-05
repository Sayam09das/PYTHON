number = int(input("Enter any number: "))
for i in range(1,11):  #[start, stop]) mean 1 is start and 11 end value. 
                        #     So, range(1, 11) includes the numbers 1, 2, 3, ..., 10. 
                        #     If you wanted to print the multiplication table up to a different number,
                        #     you could adjust the range accordingly.
    multiplication =number*i  
    print(f"{number} x {i} = {multiplication}")
