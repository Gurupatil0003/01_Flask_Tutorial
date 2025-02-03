## Topics 

- [What is Flask](#what-is-flask)
- [Install Virtual Environment](#Install-Virtual-Environment)
- [How to Install Flask](#install-flask)
- [How check Flask  Version](#Pip-version)
- [A mini_Flask application](#a-minimal-app)
- [Flask Project Structure](#flask-project-structure) - a few options
- (WIP) [Flask Bootstrap Sample](#flask-bootstrap-sample) - a simple project built with Bootstrap
- (WIP) [Jinja Template](#jinja-template) - how to render HTML pages efficiently
- [Url_Variable Rule and Creatinng_url_Examle](#Url-Rule-&-Creation-url)-What is the Rule of Variable and creation of Url


<br />

## What is Flask 

*Flask is a lightweight web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
Compared to [Django](https://www.djangoproject.com/), Flask provides a lightweight codebase and more freedom to the developer.*

## Virtual Environment
*-We use a module named virtualenv which is a tool to create isolated Python environments. virtualenv creates a folder that contains all the necessary executables to use the packages that a Python project would need.*

*-A Python Virtual Environment is an isolated space where you can work on your Python projects, separately from your system-installed Python.*

*-You can set up your own libraries and dependencies without affecting the system Python.*

*-We will use virtualenv to create a virtual environment in Python.*

## Why do we need a virtual environment?

*-Imagine a scenario where you are working on two web-based Python projects one of them uses Django 4.0 and the other uses Django 4.1 (check for the latest Django versions and so on). In such situations, we need to create a virtual environment in Python that can be really useful to maintain the dependencies of both projects.*

### Installing Virtula environment
```python
#Installing Virtula environment
pip install virtualenv
```
### Call Virutal Environment
```python
#Call Virutal Environment and it's  local directory Name  Like--- Venv or Guru or Data etc....
virtualenv venv
```
### Activate a virtual environment
```python
#Activate a virtual environment based on your OS
For windows > venv\Scripts\activate
For linux > source ./venv/bin/activate

```
#If your Facing Any error Then Try this
```python
Set-ExecutionPolicy RemoteSigned -Scope Process

```
## Install Flask

*The easiest way to install [Flask](https://palletsprojects.com/p/flask/) is to use [PIP](https://pip.pypa.io/en/stable/quickstart/) the official package-management tool.*

### Install Flask Command
```python
pip install Flask
```

<br />

## How to check Flask version

*Open a Python console or platoform (type python in terminal) and check the installed version as below:*

```python 

import flask
flask_version = flask.__version__
print(f"Installed Flask version: {flask_version}")

       Or
flask --version

```
# Mini App

[Code Here ⚙️](/minimal_app)

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=="__main__":
    app.run()

```

#### So what did that code do?

*1. First we imported the Flask class. An instance of this class will be our WSGI application.*

*2. Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate   for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.*

*3. We then use the route() decorator to tell Flask what URL should trigger our function.*

*4. The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.*

<hr>

# Debug Mode

[Code Here ⚙️](/debug_mode)

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# debug mode running on 8000 port
if __name__=="__main__":
    app.run(debug=True, port=8000)
 ```
*> The flask run command can do more than just start the development server. By enabling debug mode, the server will automatically reload if code changes, and will show an          interactive debugger in the browser if an error occurs during a request.*

*> Warning ⚠️*
*> The debugger allows executing arbitrary Python code from the browser. It is protected by a pin, but still represents a major security risk. Do not run the development server or   debugger in a production environment.*

<hr>
# Creation Routing App

[Code Here ⚙️](/routing)

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is Index Page'

@app.route('/login')
def login():
    return 'This is Login Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__=="__main__":
    app.run(debug=True)

```

> Modern web applications use meaningful URLs to help users. Users are more likely to like a page and come back if the page uses a meaningful URL they can remember and use to   directly visit a page.

> Use the `route()` decorator to bind a function to a URL.

## Rendering Templates

[Code Here ⚙️](/render_template)

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/")
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run()
    
```

```python
python filename.py
      or
start flask
 
```

#### In flask, html file are served from the 'templates' folder by default and all the static file; images, css, js, etc are served from the 'static' folder. 

> These folders should be present in the root directly of your python application

<p align="center" >
    
<img src="https://i.ibb.co/7yp0z91/app-py.png"  alt="structure" style="width:350px" />

</p>
    
<hr>

## Crl Rule and Url Creation

[Code Here ⚙️](/url_variables/README.md)

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# string
@app.route('/string/<string:value>')
def string(value):
    return f"<p>Hi this is a string value {value}</p>"

# int
@app.route('/int/<int:value>')
def int(value):
    return f"<p>Hi this is a int value {value}</p>"

# float
@app.route('/float/<float:value>')
def float(value):
    return f"<p>Hi this is a float value {value}</p>"

# path
@app.route('/path/<path:value>')
def path(value):
    return f"<p>Hi this is a path value {value}</p>"

# uuid
@app.route('/uuid/<uuid:value>')
def uuid(value):
    return f"<p>Hi this is a uuid value {value}</p>"



if __name__=="__main__":
    app.run(debug=True)
    
```

~~~python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Form Example</title>
</head>
<body>
    <h2>Enter Your Name</h2>
    <form action="/" method="POST">
        <input type="text" name="name" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>


~~~

~~~python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']  # Get data from form
        return f"<h2>Hello, {name}!</h2><a href='/'>Go Back</a>"
    return render_template('index.html')  # Render HTML form

if __name__ == '__main__':
    app.run(debug=True)


~~~
```python
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

# In-memory user storage (for simplicity)
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and check_password_hash(users[username], password):
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users:
            flash('Username already taken', 'error')
        else:
            users[username] = generate_password_hash(password)
            return redirect(url_for('login'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

```

# index Page

```python
<h1>Welcome!</h1>
<a href="/login">Login</a> | <a href="/register">Register</a>


```

# Login Page
```python

<h2>Login</h2>
<form method="POST">
    <label>Username:</label>
    <input type="text" name="username" required><br>

    <label>Password:</label>
    <input type="password" name="password" required><br>

    <button type="submit">Login</button>
</form>

<p>Don't have an account? <a href="/register">Register here</a></p>

```

# Register Page

```python
<h2>Register</h2>
<form method="POST">
    <label>Username:</label>
    <input type="text" name="username" required><br>

    <label>Password:</label>
    <input type="password" name="password" required><br>

    <button type="submit">Register</button>
</form>

<p>Already have an account? <a href="/login">Login here</a></p>

```
# Register and login page with Databse

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

# Database setup
def init_db():
    with sqlite3.connect('users.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL)''')
        conn.commit()

init_db()

# Helper function to query the database for user details
def get_user_by_username(username):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()

# Helper function to add a user to the database
def add_user(username, password):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = get_user_by_username(username)
        if user and check_password_hash(user[2], password):  # Check if password matches
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username already exists
        if get_user_by_username(username):
            flash('Username already taken', 'error')
        else:
            hashed_password = generate_password_hash(password)
            add_user(username, hashed_password)
            return redirect(url_for('login'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)


```

# Index Page
```python
<h1>Welcome!</h1>
<a href="/login">Login</a> | <a href="/register">Register</a>


````

# login Page

```python
<h2>Login</h2>
<form method="POST">
    <label>Username:</label>
    <input type="text" name="username" required><br>

    <label>Password:</label>
    <input type="password" name="password" required><br>

    <button type="submit">Login</button>
</form>

<p>Don't have an account? <a href="/register">Register here</a></p>


```

# Register Page

```python
<h2>Register</h2>
<form method="POST">
    <label>Username:</label>
    <input type="text" name="username" required><br>

    <label>Password:</label>
    <input type="password" name="password" required><br>

    <button type="submit">Register</button>
</form>

<p>Already have an account? <a href="/login">Login here</a></p>


```

# Login Redirect to home page

```python

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

# Database setup
def init_db():
    with sqlite3.connect('users.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL)''')
        conn.commit()

init_db()

# Helper function to query the database for user details
def get_user_by_username(username):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()

# Helper function to add a user to the database
def add_user(username, password):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home2')
def home2():
    # Make sure the user is logged in (for simplicity, we are not implementing sessions here)
    return render_template('home2.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = get_user_by_username(username)
        if user and check_password_hash(user[2], password):  # Check if password matches
            return redirect(url_for('home2'))  # Redirect to home2 after login
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username already exists
        if get_user_by_username(username):
            flash('Username already taken', 'error')
        else:
            hashed_password = generate_password_hash(password)
            add_user(username, hashed_password)
            return redirect(url_for('login'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
```
# index Html
```html

<h1>Welcome!</h1>
<a href="/login">Login</a> | <a href="/register">Register</a>

```
# Login Html

```python
<h2>Login</h2>
<form method="POST">
    <label>Username:</label>
    <input type="text" name="username" required><br>

    <label>Password:</label>
    <input type="password" name="password" required><br>

    <button type="submit">Login</button>
</form>

<p>Don't have an account? <a href="/register">Register here</a></p>


```

# Register Html

```html
<h2>Register</h2>
<form method="POST">
    <label>Username:</label>
    <input type="text" name="username" required><br>

    <label>Password:</label>
    <input type="password" name="password" required><br>

    <button type="submit">Register</button>
</form>

<p>Already have an account? <a href="/login">Login here</a></p>

```

# Home2.Html

```python

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Welcome!</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body class="home2">
    <div class="content">
        <h1>Welcome, you are logged in!</h1>
        <p>This is a colorful page. Enjoy your session!</p>
        <p><a href="/">Go back to the main page</a></p>
    </div>
</body>
</html>

```

