# Write a Python program that converts a given integer into its Roman numeral representation
def int_to_roman(num):
    # Define a dictionary of Roman numerals and their corresponding values
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    
    roman_num = ''
    i = 0
    
    # Convert the integer to Roman numeral
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    
    return roman_num

# Take user input
number = int(input("Enter an integer: "))

# Convert and display the Roman numeral
roman_numeral = int_to_roman(number)
print(f"The Roman numeral for {number} is {roman_numeral}")
