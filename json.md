## 📁 Super Simple Project Structure
```python
your_project/
│── app.py
│── data.json
│── templates/
│     └── index.html
└── static/
      └── script.js
```
## 🟦 1. app.py (VERY simple)
```html
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/json")
def send_json():
    with open("data.json") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
```html
## 🟩 2. templates/index.html (simple buttons + text)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Simple Flask JSON Example</title>
</head>
<body>

<h2>Simple Flask + JSON Demo</h2>

<button onclick="loadJSON()">Load JSON File</button>

<p>JSON Output:</p>
<pre id="output"></pre>

<script src="{{ url_for('static', filename='script.js') }}"></script>

</body>
</html>
```
## 🟨 3. static/script.js (super simple fetch)
```html
function loadJSON() {
    fetch("/json")
        .then(response => response.json())
        .then(data => {
            document.getElementById("output").textContent =
                JSON.stringify(data, null, 2);
        });
}
```
## 🟥 4. data.json (very small JSON)
```html
{
    "message": "Hello from JSON!",
    "number": 123
}

```
