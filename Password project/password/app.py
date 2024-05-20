from flask import Flask, request, render_template
import random
import string

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        try:
            length = int(request.form['length'])
            use_uppercase = 'uppercase' in request.form
            use_digits = 'digits' in request.form
            use_special = 'special' in request.form
            password = generate_password(length, use_uppercase, use_digits, use_special)
        except ValueError as ve:
            password = f"Error: {ve}"
        except Exception as e:
            password = f"An unexpected error occurred: {e}"

    return render_template('index.html', password=password)

if __name__ == "__main__":
    app.run(debug=True)
