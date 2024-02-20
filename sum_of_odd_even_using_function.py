def odd_even():
    sum_of_odd=0
    sum_of_even=0
    for i in range(start,end):
        if i%2==0:
            sum_of_even+=i
        else:
            sum_of_odd+=i
    print("Sum of all even number is",sum_of_even) 
    print("Sum of all odd number is",sum_of_odd)

start=int(input("Enter start number: "))
end=int(input("Enter end number: "))
odd_even()