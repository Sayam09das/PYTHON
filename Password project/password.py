import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    char_set = string.ascii_lowercase
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_digits:
        char_set += string.digits
    if use_special:
        char_set += string.punctuation
    
    if length < 1 or not char_set:
        raise ValueError("Invalid password length or character set")
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input, please try again.")

def main():
    print("Welcome to the Password Generator!")
    
    length = int(get_valid_input("Enter the desired password length: ", lambda x: x.isdigit() and int(x) > 0))
    use_uppercase = get_valid_input("Include uppercase letters? (yes/no): ", lambda x: x.lower() in ['yes', 'no']).strip().lower() == 'yes'
    use_digits = get_valid_input("Include digits? (yes/no): ", lambda x: x.lower() in ['yes', 'no']).strip().lower() == 'yes'
    use_special = get_valid_input("Include special characters? (yes/no): ", lambda x: x.lower() in ['yes', 'no']).strip().lower() == 'yes'
    
    try:
        password = generate_password(length, use_uppercase, use_digits, use_special)
        print(f"Generated Password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
