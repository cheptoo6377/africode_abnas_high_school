from flask import Flask


from flask_restful import Api
from app.resources.user import User,Users
from app.resources.teacher import Teachers,Teacher
from app.resources.student import Students,Student
from app.resources.fee import Fees,Fee
from app.resources.enrolment import Enrolments,Enrolment
from app.resources.course import Courses,Course
from app.extension import db

from config import Config
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
api = Api(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "School Management System"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

migrate = Migrate(app, db)







   #api endpoints

api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')
api.add_resource(Teachers, '/api/teachers')
api.add_resource(Teacher, '/api/teachers/<int:id>')
api.add_resource(Students, '/api/students')
api.add_resource(Student, '/api/students/<int:id>')
api.add_resource(Fees, '/api/fees')
api.add_resource(Fee, '/api/fees/<int:id>')
api.add_resource(Enrolments, '/api/enrolments')
api.add_resource(Enrolment, '/api/enrolments/<int:id>')
api.add_resource(Courses, '/api/courses')
api.add_resource(Course, '/api/courses/<int:id>')