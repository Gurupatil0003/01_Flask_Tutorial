```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['hotel_booking']

# Clear old data (optional)
db.hotels.delete_many({})

# Sample hotel data
hotels_data = [
    {
        "name": "Taj Hotel",
        "location": "Mumbai",
        "price": 5000,
        "image": "static/hotel_images/d.jpg"
    },
    {
        "name": "Oberoi Hotel",
        "location": "Delhi",
        "price": 4500,
        "image": "static/hotel_images/images (2).jpg"
    },
    {
        "name": "Leela Palace",
        "location": "Bangalore",
        "price": 6000,
        "image": "static/hotel_images/images (3).jpg"
    }
]

# Insert data into MongoDB
db.hotels.insert_many(hotels_data)

print("Hotels inserted successfully!")

```

```python
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import gridfs

app = Flask(__name__)

# --------------------------
# MongoDB Setup
# --------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client['hotel_booking']
users = db["users"]
hotels = db["hotels"]  # make sure you have hotel data here
fs = gridfs.GridFS(db)


# --------------------------
# LOGIN
# --------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = users.find_one({"username": username, "password": password})

        if user:
            return redirect(url_for("dashboard"))
        return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


# --------------------------
# REGISTER
# --------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if users.find_one({"username": username}):
            return render_template("register.html", error="Username already exists")

        users.insert_one({"username": username, "password": password})
        return redirect(url_for("login"))

    return render_template("register.html")


# --------------------------
# DASHBOARD
# --------------------------
@app.route("/dashboard")
def dashboard():
    hotel_list = list(hotels.find())
    for hotel in hotel_list:
        hotel['_id'] = str(hotel['_id'])  # convert ObjectId to string for template
    return render_template("hotels.html", hotels=hotel_list)


# --------------------------
# RUN APP
# --------------------------
if __name__ == "__main__":
    app.run(debug=True, port=8000)


```

```python
<!DOCTYPE html>
<html>
<head>
    <title>Hotel Dashboard</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='d.css') }}">
</head>
<body>

    <h1>Hotel Dashboard</h1>

    {% for hotel in hotels %}
    <div class="hotel-card">
        <h2>{{ hotel.name }}</h2>
        <p>Location: {{ hotel.location }}</p>
        <p>Price: ₹{{ hotel.price }}</p>
        <img src="{{ hotel.image }}" alt="{{ hotel.name }} image">
    </div>
    {% endfor %}

</body>
</html>


```

```python
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='login.css') }}">
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>

        {% if error %}
            <p class="error-message">{{ error }}</p>
        {% endif %}

        <form method="post">
            <input name="username" placeholder="Username"><br>
            <input name="password" type="password" placeholder="Password"><br>
            <button type="submit">Login</button>
        </form>

        <a href="{{ url_for('register') }}">Register</a>
    </div>
</body>
</html>


```

```python
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='login.css') }}">
</head>
<body>
    <div class="login-container">
        <h2>Register</h2>

        {% if error %}
            <p class="error-message">{{ error }}</p>
        {% endif %}

        <form method="post">
            <input name="username" placeholder="Choose Username"><br>
            <input name="password" type="password" placeholder="Choose Password"><br>
            <button type="submit">Register</button>
        </form>

        <a href="{{ url_for('login') }}">Login</a>
    </div>
</body>
</html>


```

## styles.css

```python
/* -------------------------
   Reset & Basic Styling
------------------------- */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f0f2f5;
    margin: 0;
    padding: 0;
}

/* -------------------------
   Top Navigation
------------------------- */
.top-nav {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    padding: 15px 30px;
    background-color: #1e90ff;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.top-nav a {
    color: #fff;
    text-decoration: none;
    font-weight: 600;
    margin-left: 20px;
    transition: all 0.3s ease;
}

.top-nav a:hover {
    text-decoration: underline;
    color: #ffd700;
}

/* -------------------------
   Page Title
------------------------- */
h1 {
    text-align: center;
    color: #333;
    margin-top: 30px;
}

/* -------------------------
   Hotel Cards
------------------------- */
.hotel-card {
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    margin: 20px auto;
    padding: 20px;
    width: 350px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hotel-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.2);
}

.hotel-card img {
    border-radius: 10px;
    margin-bottom: 15px;
    width: 100%;
    height: 200px;
    object-fit: cover;
}

/* -------------------------
   Booking Form
------------------------- */
input[type="text"] {
    width: 70%;
    padding: 8px 10px;
    border-radius: 8px;
    border: 1px solid #ccc;
    margin-bottom: 10px;
    transition: all 0.3s ease;
}

input[type="text"]:focus {
    border-color: #1e90ff;
    outline: none;
    box-shadow: 0 0 5px rgba(30,144,255,0.5);
}

button {
    padding: 8px 15px;
    background-color: #1e90ff;
    color: #fff;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
}

button:hover {
    background-color: #ffb700;
    color: #000;
}

p#msg-1, p#msg-2, p#msg-3 {
    font-weight: bold;
}


```

## login.css
```python

/* -------------------------
   Login/Register Page
------------------------- */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f0f2f5;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.login-container {
    background-color: #fff;
    padding: 40px 30px;
    border-radius: 12px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.1);
    width: 350px;
    text-align: center;
}

.login-container h2 {
    margin-bottom: 25px;
    color: #333;
}

.login-container input {
    width: 90%;
    padding: 10px;
    margin: 10px 0;
    border-radius: 8px;
    border: 1px solid #ccc;
    transition: all 0.3s ease;
}

.login-container input:focus {
    border-color: #1e90ff;
    outline: none;
    box-shadow: 0 0 5px rgba(30,144,255,0.5);
}

.login-container button {
    width: 95%;
    padding: 10px;
    margin-top: 15px;
    border: none;
    border-radius: 8px;
    background-color: #1e90ff;
    color: #fff;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
}

.login-container button:hover {
    background-color: #ffb700;
    color: #000;
}

.login-container a {
    display: block;
    margin-top: 15px;
    text-decoration: none;
    color: #1e90ff;
    font-weight: 600;
    transition: all 0.3s ease;
}

.login-container a:hover {
    color: #ffb700;
    text-decoration: underline;
}

.error-message {
    color: red;
    font-weight: bold;
    margin-bottom: 10px;
}



```
# d.css
```python
/* -------------------------
   Body & Page Styling
------------------------- */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #fdfbfb, #ebedee);
    margin: 0;
    padding: 0;
}

/* -------------------------
   Page Title
------------------------- */
h1 {
    text-align: center;
    color: #1e90ff;
    font-size: 3rem;
    margin: 40px 0 20px 0;
    animation: fadeInDown 1s ease forwards;
}

/* -------------------------
   Hotel Cards Container
------------------------- */
.hotel-card {
    background-color: #fff;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    margin: 30px auto;
    padding: 25px;
    width: 350px;
    text-align: center;
    transform: translateY(0);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    animation: fadeInUp 1s ease forwards;
}

/* Floating hover effect */
.hotel-card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 20px 35px rgba(0,0,0,0.2);
}

/* -------------------------
   Hotel Image
------------------------- */
.hotel-card img {
    border-radius: 12px;
    width: 100%;
    height: 220px;
    object-fit: cover;
    margin-bottom: 15px;
    transition: transform 0.5s ease;
}

.hotel-card img:hover {
    transform: scale(1.05) rotate(1deg);
}

/* -------------------------
   Hotel Info Text
------------------------- */
.hotel-card h2 {
    margin-bottom: 10px;
    color: #1e90ff;
    font-size: 1.6rem;
    transition: color 0.3s ease;
}

.hotel-card h2:hover {
    color: #ff7f50;
}

.hotel-card p {
    margin: 5px 0;
    color: #555;
    font-weight: 500;
}

/* -------------------------
   Animations
------------------------- */
@keyframes fadeInDown {
    0% { opacity: 0; transform: translateY(-30px);}
    100% { opacity: 1; transform: translateY(0);}
}

@keyframes fadeInUp {
    0% { opacity: 0; transform: translateY(30px);}
    100% { opacity: 1; transform: translateY(0);}
}

```
