from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Here you would typically process form data and add the user to the database
        # For simplicity, we'll just print the data to the console
        username = request.form['username']
        password = request.form['password']
        print(f"Registered user: {username} with password: {password}")
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you would typically check credentials against the database
        # For simplicity, we'll just print the data to the console
        username = request.form['username']
        password = request.form['password']
        print(f"Login attempt with username: {username} and password: {password}")
        return redirect(url_for('home'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
