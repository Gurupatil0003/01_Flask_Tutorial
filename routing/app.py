from flask import Flask

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, this is the home page!'

# Define a route for another page
@app.route('/about')
def about():
    return 'This is the about page.'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
