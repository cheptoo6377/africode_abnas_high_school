from flask_restful import Resource, marshal_with, fields, abort, reqparse
from app.models import StudentModel
from app.extension import db
from dateutil.parser import parse as date_parse



student_args = reqparse.RequestParser()
student_args.add_argument('first_name', type=str, required=True, help="firstname is required")
student_args.add_argument('last_name', type=str, required=True, help="lastname is required")
student_args.add_argument('student_id', type=str, required=True, help="student_id is required")
student_args.add_argument('email', type=str, required=True, help="email is required")
student_args.add_argument('date_of_birth', type=date_parse)
student_args.add_argument('enrolment_date', type=date_parse)

student_fields={
'id': fields.Integer,
'first_name': fields.String,
'last_name': fields.String,
'student_id': fields.String,
'email': fields.String,
'date_of_birth': fields.String,
'enrolment_date': fields.String


}


class Students(Resource):
    @marshal_with(student_fields)
    def get(self):
        student = StudentModel.query.all()
        if not student:
            abort(404, message='student not found')
        return student
    
    @marshal_with(student_fields)
    def post(self):
        args = student_args.parse_args

        try:
            new_student = StudentModel(first_name=args['first_name'], last_name=args['last_name'], student_id=args['student_id'], email=args['email'], date_of_birth=args['date_of_birth'], enrolment_date=args['enrolment_date'])
            db.session.add(new_student)
            db.session.commit()
            return new_student, 201
        except Exception as e:
            db.session.rollback()
            abort(400, message=f"error creating a student {str(e)}")


class Student(Resource):
        @marshal_with(student_fields)
        def get(self, id):
            student = StudentModel.query.filter_by(id=id).first()
            
            if not student:
                abort(404, message='student not found')
            return student
        @marshal_with(student_fields)
        def patch(self, id):
         args = student_args.parse_args()
         student = StudentModel.query.filter_by(id=id).first()
         if not student:
            abort(404, message="Student with that id not found")
         student.first_name = args["first_name"]
         student.last_name = args["last_name"]
         student.student_id = args["student_id"]
         student.email = args["email"]
         student.date_of_birth = args["date_of_birth"]
         student.enrolment_date = args["enrolment_date"]
         db.session.commit()
         return student

        @marshal_with(student_fields)
        def delete(self, id):
            student = StudentModel.query.filter_by(id=id).first()
            if not student:
                abort(404, message="cannot delete this student")
            db.session.delete(student)
            db.session.commit()
      




        

