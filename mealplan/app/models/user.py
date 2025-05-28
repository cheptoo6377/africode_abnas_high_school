from app import db
from flask_login import UserMixin
from flask_login import LoginManager

from datetime import datetime



class UserModel(db.Model, UserMixin):
  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False ,unique=True)
    firstname = db.Column(db.String(50), nullable=False)  
    lastname = db.Column(db.String(50), nullable=False)   
    password = db.Column(db.String(100), nullable=False)
    meal = db.relationship('Mealplan', backref='user', lazy=True)
    def __repr__(self):
        return f'{self.firstname}'