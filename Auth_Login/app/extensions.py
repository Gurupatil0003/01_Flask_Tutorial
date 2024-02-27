# Flask modules
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "routes.login"
login_manager.login_message_category = "info" 

login page but I will be ready to go 
