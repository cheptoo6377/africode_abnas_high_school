from app import db, login_manager
from flask_login import UserMixin

from datetime import datetime,timedelta

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin ):
  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False ,unique=True)
    firstname = db.Column(db.String(50), nullable=False)  # Uncommented firstname
    lastname = db.Column(db.String(50), nullable=False)   # Uncommented lastname
    password = db.Column(db.String(100), nullable=False)
    meal = db.relationship('Mealplan', backref='user', lazy=True)
    def __repr__(self):
        return f'{self.firstname}'

class Mealplan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.column(db.DateTime, nullable= False)
    breakfast = db.Column(db.String(100), nullable=False)
    snack = db.Column(db.String(100), nullable=False)
    lunch = db.Column(db.String(100), nullable=False)
    dinner = db.Column(db.String(100), nullable=False)
    supper = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))