
# Flask Email & Authentication App

This project is a Flask web application that provides user registration, login, and email-sending functionality. It is built with a modern, attractive UI featuring advanced CSS animations and 3D effects.

## Overview

- **User Registration & Login:**  
  Secure authentication using MySQL as the database and Flask-Bcrypt for password hashing.

- **Email Sending:**  
  Users can send emails from within the application. The project is configured to use Mailtrap for testing, so no real emails are sent during development.

- **Modern UI:**  
  The interface uses custom CSS with glassmorphism, smooth 3D animations, and interactive elements to create an immersive user experience.

- **Flash Notifications:**  
  Real-time flash messages and a success popup inform users of their actions.

## Project Structure




## Features Explained

### User Authentication
- **Registration (`/register`):**  
  New users can sign up by providing a username and password. Passwords are hashed using Flask-Bcrypt before being stored in the MySQL database.
  
- **Login (`/login`):**  
  Registered users can log in with their credentials. Sessions are used to manage user authentication.

- **Logout (`/logout`):**  
  Users can log out, which clears their session.

### Email Sending
- **Email Form (`/`):**  
  Authenticated users can send emails by entering the recipient’s email, subject, and message.
  
- **Email Processing (`/send_mail`):**  
  The application sends emails using Flask-Mail. For development, it uses Mailtrap’s SMTP settings so that emails are captured in a safe testing environment.

- **Success Notification (`/success`):**  
  After sending an email, the user is redirected to a success page that shows an animated popup confirming that the email was sent.

### Modern UI and CSS Animations
- **Glassmorphism & 3D Effects:**  
  The UI features a modern glass-like effect with blurred backgrounds and smooth, 3D transitions.
  
- **Interactive Elements:**  
  Buttons and inputs have neon glow and scaling effects to create an engaging user experience.
  
- **Animated Success Popup:**  
  The success page uses keyframe animations (bounce and 3D rotation) to provide a dynamic confirmation message.

## Installation

### Prerequisites
- Python 3.8+
- MySQL Server installed and running
- Mailtrap account (for testing emails) or production SMTP credentials if sending real emails
- `pip` for installing Python dependencies

### Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
## Install Dependencies:

```python
pip install -r requirements.txt
```

# create Databse in Mysql Workbench
```Mysql

CREATE DATABASE flask_app;
USE flask_app;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE email_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    recipient VARCHAR(255) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    body TEXT NOT NULL
);


select * from user;

```

# Session:
- A session is like a temporary storage for user data while they are using a website. It helps the website remember who  the user is after they log in.

Example:

- You log into a website.
- The site keeps your login information in a session so you don’t have to log in again on every page.
 When you log out, the session is cleared.

# Cookies:
- A cookie is a small piece of data stored in your browser by a website. It helps websites remember things even after    you close the browser.

Example:

- You visit an online store, add items to your cart, and close the browser.
- When you come back later, the items are still in your cart because the website stored them in a cookie.

