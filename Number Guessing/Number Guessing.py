import random

def main():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")

    # Loop until the user guesses the correct number
    while guess != number_to_guess:
        # Prompt the user for a guess
        guess = input("Enter your guess: ")

        # Validate the input
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Increment the number of attempts
        attempts += 1

        # Provide feedback
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")

if __name__ == "__main__":
    main()
