from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# SQLite Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Mail Configuration (Using Mailtrap)
app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '2fb1fa63154125'
app.config['MAIL_PASSWORD'] = 'deef2a3e606422'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Home Page (Only Accessible After Login)
@app.route('/')
def home():
    if 'user' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already taken! Try another.", "error")
            return redirect(url_for('register'))

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            session['user'] = username
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials! Try again.", "error")

    return render_template('login.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# Send Email Page
@app.route('/send_mail', methods=['POST'])
def send_mail():
    try:
        if 'user' not in session:
            flash("You must be logged in to send emails!", "error")
            return redirect(url_for('login'))

        recipient = request.form.get('recipient')
        subject = request.form.get('subject')
        body = request.form.get('body')

        if not recipient or not subject or not body:
            flash("All fields are required!", "error")
            return redirect(url_for('home'))

        msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
        msg.body = body
        mail.send(msg)

        return render_template('success.html')  # ✅ Redirects to success page

    except Exception as e:
        flash(f"Error sending email: {str(e)}", "error")
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
