from app.extension import db


from datetime import datetime



class MealplanModel(db.Model,datetime):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    breakfast = db.Column(db.String(100), nullable=False)
    snack = db.Column(db.String(100), nullable=False)
    lunch = db.Column(db.String(100), nullable=False)
    dinner = db.Column(db.String(100), nullable=False)
    supper = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))