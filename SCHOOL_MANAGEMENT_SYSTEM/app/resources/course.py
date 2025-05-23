from flask_restful import Resource, marshal_with, fields, abort, reqparse
from app.models import CourseModel
from app.extension import db


course_args = reqparse.RequestParser()
course_args.add_argument('code', type=str, required=True, help="course_code is required")
course_args.add_argument('name', type=str, required=True, help="course_name is required")
course_args.add_argument('credits', type=int, required=True, help="credits is required")
course_args.add_argument('teacher_id', type=int, required=True, help="teacher_id is required")


course_fields = {
    'id': fields.Integer,
    'code': fields.String,
    'name': fields.String,
    'credits': fields.Integer,
    'teacher_id': fields.Integer
    
}
class Courses(Resource):
    @marshal_with(course_fields)
    def get(self):
        courses = CourseModel.query.all()
        if not courses:
            abort(404, message='cannot find course')
        return courses
    
    @marshal_with(course_fields)
    def post(self):
        args = course_args.parse_args()

        try:
            new_course = CourseModel(code=args['code'], name=args['name'], credits=args['credits'], teacher_id=args['teacher_id'])
            db.session.add(new_course)
            db.session.commit()
            return new_course, 201
        except Exception as e:
            db.session.rollback()
            abort(400, message=f"error creating a course {str(e)}")
class Course(Resource):
    @marshal_with(course_fields)
    def get(self, id):
        course = CourseModel.query.filter_by(id=id).first()
        
        if not course:
            abort(404, message='course not found')
        return course
    
    @marshal_with(course_fields)
    def patch(self, id):
        args = course_args.parse_args()
        course = CourseModel.query.filter_by(id=id).first()
        if not course:
            abort(404, message='course not found')
        course.code = args['code']
        course.name = args['name']
        course.credits = args['credits']
        db.session.commit()
        return course
    @marshal_with(course_fields)
    def delete(self, id):
        course = CourseModel.query.filter_by(id=id).first()
        if not course:
            abort(404, message='course not found')
        db.session.delete(course)
        db.session.commit()
        return '', 204