from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Handle user login data (e.g., validate credentials)
        username = request.form.get('username')
        # Process the data as needed
        return f"Welcome, {username}!"
    else:
        # Display the login form
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
