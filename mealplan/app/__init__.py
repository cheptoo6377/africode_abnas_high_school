from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
from app.resources.mealplan import Mealplan,Mealplans
from app.resources.user import Users,User
from app.extension import db

from config import Config


app = Flask(__name__)

app.config['SECRET_KEY'] = '9c7122e76a4f0cdd13813494547ab17b00623d13d2e51016479f1f1e49e9d525'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "info"






app.config.from_object(Config)


db.init_app(app)
api = Api(app)



api.add_resource(Users, '/api/users')
api.add_resource(User, '/api/users/<int:id>')
api.add_resource(Mealplans, '/api/mealplans')
api.add_resource(Mealplan, '/api/mealplans/<int:id>')
