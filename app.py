import os, random
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Credentials
valid_username = "Cee404"
valid_password = "I124Q"

@app.route('/')
def home():
    # Debug line to check the template folder path
    print("Template folder path:", os.path.join(os.getcwd(), "templates"))
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cee')
def cee():
    return render_template('cee.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check credentials
        if username == valid_username and password == valid_password:
            return render_template('lab.html', username=username)
        else:
            error = "Invalid username or password. Try again."
            return render_template('login.html', error=error)

    return render_template('login.html')

# List of random fortunes/stories
fortunes = [
    "You will have a great coding session today!",
    "An unexpected opportunity will come your way.",
    "Beware of bugs in your code—they multiply when untested!",
    "You will soon solve a problem that's been bothering you.",
    "A friend will surprise you with good news."
]

@app.route('/Story', methods=['GET'])
def Story():
    return jsonify({"fortune": random.choice(fortunes)})
if __name__ == '__main__':
    app.run(debug=True)
