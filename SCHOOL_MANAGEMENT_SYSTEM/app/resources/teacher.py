from flask_restful import Resource,marshal_with,fields,abort,reqparse
from app.models.teacher import TeacherModel
from app.extension import db

teacher_args = reqparse.RequestParser()
teacher_args.add_argument('first_name',type=str,required=True,help="firstname is required")
teacher_args.add_argument('last_name',type=str,required=True,help="lastname is required")
teacher_args.add_argument('email',type=str,required=True,help="email is required")
teacher_args.add_argument('phone',type=str)
teacher_args.add_argument('department',type=str)
teacher_args.add_argument('courses',type=str)
teacher_args.add_argument('credits',type=int,help="credits is required")


teacher_fields = {
   'id': fields.Integer,
   'first_name': fields.String,
   'last_name': fields.String,
    'email': fields.String,
    'phone': fields.String,
    'department': fields.String,
    'courses': fields.String,
    'hire_date': fields.DateTime,
    'credits': fields.Integer
   
}


class Teachers(Resource):
    @marshal_with(teacher_fields)
    def get(self):
     teachers = TeacherModel.query.all()
     if not teachers:
        abort(404,message= 'cannot find teacher')
     return teachers
    
    @marshal_with(teacher_fields)
    def post(self):
       
       args = teacher_args.parse_args()
       try:
          new_teacher = TeacherModel(first_name=args['first_name'],last_name=args['last_name'],email=args['email'],credits=args['credits'],phone=args['phone'],department=args['department'])
          db.session.add(new_teacher)
          db.session.commit()
          return new_teacher,201
       except Exception as e:
          db.session.rollback
          abort(400,message=f"error creating a teacher{str(e)}")

class Teacher(Resource):
    @marshal_with(teacher_fields)
    def get(self, id):
        teacher = TeacherModel.query.filter_by(id=id).first()
        
        if not teacher:
            abort(404, message='teacher not found')
        return teacher
   

   
   
    @marshal_with(teacher_fields)
    def patch(self, id):
         args = teacher_args.parse_args()
         teacher = TeacherModel.query.filter_by(id=id).first()
         if not teacher:
            abort(404, message="Teacher with that id not found")
         teacher.first_name = args["first_name"]
         teacher.last_name = args["last_name"]
         teacher.email = args["email"]
         teacher.phone = args["phone"]
         teacher.department = args["department"]
         teacher.credits = args["credits"]
         db.session.commit()
         return teacher 
    @marshal_with(teacher_fields)
    def delete(self, id):
        teacher = TeacherModel.query.filter_by(id=id).first()
        if not teacher:
            abort(404, message="cannot delete this teacher")
        db.session.delete(teacher)
        db.session.commit()
        
      
