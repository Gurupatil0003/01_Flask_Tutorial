from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Set up the database URI (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

# Initialize the database object
db = SQLAlchemy(app)

# Define the model (User table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(100), nullable=False)

# Route for home page
@app.route('/')
def index():
    # Query all users from the database
    users = User.query.all()
    return render_template('index.html', users=users)

# Ensure the database is created and insert sample users if needed
with app.app_context():
    db.create_all()

    # Add users only if there are no records
    if User.query.count() == 0:
        user1 = User(name='John Doe', age=28, city='New York')
        user2 = User(name='Jane Smith', age=34, city='San Francisco')
        db.session.add_all([user1, user2])
        db.session.commit()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
