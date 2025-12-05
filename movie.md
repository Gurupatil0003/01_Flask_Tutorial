```python
from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

def load_movies():
    with open("movies.json", "r") as f:
        return json.load(f)

@app.route("/")
def dashboard():
    movies = load_movies()[:4]  # first 4 movies for dashboard
    return render_template("dashboard.html", movies=movies)

@app.route("/recommender")
def recommender():
    return render_template("index.html")

@app.route("/recommend")
def recommend():
    movies = load_movies()
    
    selected_movie = random.choice(movies)
    return jsonify(selected_movie)

if __name__ == "__main__":
    app.run(debug=True)

```

# dashboard.html
```python
<!DOCTYPE html>
<html>
<head>
    <title>Movie Dashboard 🎬</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='dashboard.css') }}">
</head>
<body>

<h1 class="title">🎬 Movie Dashboard</h1>

<div class="grid">
    {% for m in movies %}
    <div class="card">
        <img src="{{ url_for('static', filename=m.image) }}">
        <h3>{{ m.title }}</h3>
        <p class="category">{{ m.category }}</p>

        <!-- Small booking interface -->
        <div class="booking">
            <label>Seats:</label>
            <input type="number" min="1" max="10" value="1">
            <button onclick="bookMovie('{{ m.title }}')">Book</button>
        </div>

        <!-- Extra buttons -->
        <div class="extra-buttons">
            <button onclick="viewDetails('{{ m.title }}')">View Details</button>
            <button onclick="addFavorite('{{ m.title }}')">Add to Favorites</button>
            <button onclick="watchTrailer('{{ m.title }}')">Watch Trailer</button>
        </div>
    </div>
    {% endfor %}
</div>

<div class="actions">
    <a href="/recommender"><button class="btn">Go to Movie Recommender</button></a>
</div>

<script src="/static/script.js"></script>

</body>
</html>


```

## index.html
```python
<!DOCTYPE html>
<html>
<head>
    <title>Movie Recommender 🎬</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

<div class="container">
    <h1>Simple Movie Recommender</h1>

    <img id="movieImage" src="{{ url_for('static', filename='movies/movie1.jpg') }}" alt="Movie Poster">

    <h2 id="movieTitle">Click the button to get a movie!</h2>

    <button onclick="getMovie()">Recommend Movie</button>
</div>

<script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>


```

## script.html
```python
function getMovie() {
    fetch(`/recommend`)
    .then(response => response.json())
    .then(data => {
        document.getElementById("movieTitle").innerText = data.title;
        document.getElementById("movieImage").src = `/static/${data.image}`;
    });
}


function bookMovie(title) {
    const seats = event.target.previousElementSibling.value;
    alert(`Successfully booked ${seats} seat(s) for ${title}! 🎉`);
}

function viewDetails(title) {
    alert(`Details of ${title}:\nGenre: Example Genre\nRating: ⭐⭐⭐⭐`);
}

function addFavorite(title) {
    alert(`${title} added to your favorites! ❤️`);
}

function watchTrailer(title) {
    alert(`Opening trailer for ${title}... 🎬`);
}

```

## dashboard.css

```python
/* Body & background */
body {
    background: linear-gradient(to bottom right, #e0f7fa, #ffe0b2);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    text-align: center;
    padding: 50px 20px;
    margin: 0;
}

/* Page title */
.title {
    font-size: 38px;
    color: #333;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    margin-bottom: 40px;
}

/* Grid layout */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 25px;
    max-width: 900px;
    margin: 0 auto;
}

/* Movie card */
.card {
    background: #fff;
    border-radius: 15px;
    padding: 15px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
    position: relative;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 25px rgba(0,0,0,0.2);
}

/* Movie poster image */
.card img {
    width: 100%;
    border-radius: 12px;
    margin-bottom: 12px;
    transition: transform 0.3s;
}

.card img:hover {
    transform: scale(1.03);
}

/* Movie title */
.card h3 {
    margin: 10px 0 5px;
    font-size: 20px;
    color: #222;
}

/* Category badge */
.category {
    display: inline-block;
    background: #ffca28;
    color: #333;
    font-size: 13px;
    font-weight: bold;
    padding: 3px 10px;
    border-radius: 12px;
    margin-bottom: 12px;
}

/* Booking input & button */
.booking input {
    width: 50px;
    padding: 6px;
    margin-right: 6px;
    border-radius: 6px;
    border: 1px solid #ccc;
}

.booking button {
    padding: 6px 14px;
    cursor: pointer;
    background: #43a047;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 13px;
    transition: background 0.3s, transform 0.2s;
}

.booking button:hover {
    background: #2e7d32;
    transform: scale(1.05);
}

/* Extra buttons */
.extra-buttons {
    margin-top: 12px;
}

.extra-buttons button {
    padding: 6px 12px;
    margin: 4px 3px;
    border: none;
    border-radius: 8px;
    font-size: 13px;
    cursor: pointer;
    background: #1976d2;
    color: white;
    transition: background 0.3s, transform 0.2s;
}

.extra-buttons button:hover {
    background: #0d47a1;
    transform: scale(1.05);
}

/* Dashboard actions button */
.actions {
    margin-top: 40px;
}

.btn {
    padding: 14px 28px;
    font-size: 18px;
    cursor: pointer;
    border: none;
    border-radius: 10px;
    background: #0288d1;
    color: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    transition: background 0.3s, transform 0.2s;
}

.btn:hover {
    background: #01579b;
    transform: scale(1.05);
}

/* Responsive adjustments */
@media (max-width: 480px) {
    .grid {
        grid-template-columns: 1fr;
    }
}


```

## style.css

```python
body {
    margin: 0;
    padding: 0;
    font-family: 'Arial', sans-serif;
    background: linear-gradient(to right, #6a11cb, #2575fc);
    color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.container {
    background: rgba(0,0,0,0.7);
    padding: 30px 40px;
    border-radius: 15px;
    text-align: center;
    max-width: 400px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    transition: transform 0.3s;
}

.container:hover {
    transform: scale(1.02);
}

.container h1 {
    margin-bottom: 25px;
    font-size: 28px;
    text-shadow: 1px 1px 3px #000;
}

#movieImage {
    width: 100%;
    border-radius: 12px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.5);
    margin-bottom: 20px;
    transition: transform 0.3s;
}

#movieImage:hover {
    transform: scale(1.05);
}

#movieTitle {
    margin-bottom: 10px;
    font-size: 20px;
}

#movieDescription {
    font-size: 16px;
    color: #ddd;
    margin-bottom: 20px;
}

button {
    padding: 12px 25px;
    font-size: 16px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    background: #ff4b2b;
    color: white;
    transition: background 0.3s, transform 0.2s;
}

button:hover {
    background: #ff416c;
    transform: scale(1.05);
}

@media (max-width: 480px) {
    .container {
        padding: 20px;
    }
    #movieTitle {
        font-size: 18px;
    }
}


```

## json


```python
[
    {
        "title": "Inception",
        "image": "movies/movie1.jpg"
    },
    {
        "title": "Interstellar",
        "image": "movies/movie2.jpg"
    },
    {
        "title": "The Dark Knight",
        "image": "movies/movie3.jpg"
    },
    {
        "title": "Avatar",
        "image": "movies/movie4.jpg"
    },
    {
        "title": "Avengers Endgame",
        "image": "movies/movie5.jpg"
    },
    {
        "title": "Avengers Endgame",
        "image": "movies/movie5.jpg"
    }
]


```





```python
body {
    background: linear-gradient(to bottom, #f2f2f2, #e0e0ff);
    font-family: Arial, sans-serif;
    text-align: center;
    padding-bottom: 50px;
}

.title {
    margin-top: 20px;
    font-size: 36px;
    color: #333;
    text-shadow: 1px 1px #aaa;
}

.grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 25px;
    max-width: 700px;
    margin: 30px auto;
}

.card {
    background: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 6px 12px rgba(0,0,0,0.2);
    transition: transform 0.2s;
}

.card:hover {
    transform: translateY(-5px);
}

.card img {
    width: 100%;
    border-radius: 10px;
}

.card h3 {
    margin: 10px 0 5px;
    color: #222;
}

.category {
    font-size: 14px;
    color: #555;
    margin-bottom: 10px;
    font-weight: bold;
}

.booking input {
    width: 50px;
    padding: 5px;
    margin-right: 5px;
}

.booking button {
    padding: 5px 12px;
    cursor: pointer;
    background: #28a745;
    color: white;
    border: none;
    border-radius: 6px;
    margin-top: 5px;
}

.booking button:hover {
    background: #218838;
}

.extra-buttons {
    margin-top: 10px;
}

.extra-buttons button {
    padding: 5px 10px;
    margin: 5px 3px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    background: #007bff;
    color: white;
    font-size: 13px;
}

.extra-buttons button:hover {
    background: #0056b3;
}

.actions {
    margin-top: 30px;
}

.btn {
    padding: 12px 25px;
    font-size: 18px;
    cursor: pointer;
    border: none;
    background: #007bff;
    color: white;
    border-radius: 8px;
}

.btn:hover {
    background: #0056b3;
}


```

```python

body {
    background: #f2f2f2;
    font-family: Arial, sans-serif;
    text-align: center;
}

.container {
    margin-top: 50px;
}

img {
    width: 300px;
    border-radius: 12px;
    margin: 20px 0;
}

button {
    padding: 12px 25px;
    font-size: 18px;
    cursor: pointer;
    border: none;
    background: #333;
    color: white;
    border-radius: 8px;
}

button:hover {
    background: #555;
}

select {
    padding: 10px;
    font-size: 16px;
    margin-bottom: 20px;
}

```


