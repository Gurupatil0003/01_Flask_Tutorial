# Flask modules
#from flask_login import UserMixin
wg6ebeye r f
# Other modules
from datetime import datetime

# Local modulese te e e e6 w
from app.extensions import db

hwheur r heuiebeue euebdye is e eueneu 2ud 
#class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
#    name = db.Column(db.String(80), nullable=False)ebdfwy e
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTie eveme, default=datetime.utcnow)ebebeb

    def __repr__(self): de eg3 
        return f'<User {self.name}>'
e
hello Python syllabus 
__all__ = [User, ]vwg2 2 2
