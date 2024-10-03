# Joke Generator using Python

import requests

def joke_gen():
    url = "https://icanhazdadjoke.com/"  
    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)  # Sending a GET request to the joke API
    
    if response.status_code == 200:      # Check if the response status code is 200 (OK)
        joke_data = response.json()
        return joke_data["joke"]
    else:
        return "Oops! Couldn't fetch a joke at the moment."

def main_joke():
    print("Welcome to the Joke Generator!")
    while True:
        user_input = input("Would you like to hear a joke? (y/n): ").lower()

        if user_input == "n":
            print("Thanks for using the Joke Generator. Goodbye!")
            break
        else:
            joke = joke_gen()
            print("\nHere's a joke for you:")
            print(joke)
            print("-"*100)

if __name__ == "__main__":
    main_joke()
