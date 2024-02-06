from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# debud mode running on 8000 port
if __name__=="__main__":
    app.run(debug=True, port=8000)
