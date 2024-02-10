# Write a python to enter a number from 1-7 and display the corresponing day of the week.

def week():
    print("Enter any number from 1 to 7:")
    day = int(input())
    if day == 1:
        print("Sunday")
    elif day == 2:
        print("Monday")
    elif day == 3:
        print("Tuesday")
    elif day == 4:
        print("Wednesday")
    elif day == 5:
        print("Thursday")
    elif day == 6:
        print("Friday")
    elif day == 7:
        print("Saturday")
    else:
        print("Please enter a number between 1 and 7.")

week()
