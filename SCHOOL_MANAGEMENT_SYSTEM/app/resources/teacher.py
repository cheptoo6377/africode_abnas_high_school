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
   
   
    @marshal_with(teacher_fields)
    def patch(self, id):
         args = teacher_args.parse_args()
         teacher = TeacherModel.query.filter_by(id=id).first()
         if not teacher:
            abort(404, message="Teacher with that id not found")
         teacher.first_name = args["first_name"]
         teacher.last_name = args["last_name"]
    @marshal_with(teacher_fields)
    def delete(self, id):
        teacher = TeacherModel.query.filter_by(id=id).first()
        if not teacher:
            abort(404, message="cannot delete this teacher")
        db.session.delete(teacher)
        db.session.commit()
        
  


teacher_args = reqparse.RequestParser()
teacher_args.add_argument('first_name', type=str, required=True, help="First name is required" )
teacher_args.add_argument('last_name', type=str, required=True, help="Last name is required" )
teacher_args.add_argument('email', type=str, required=True, help="Email is required" )
teacher_args.add_argument('phone', type=str)
teacher_args.add_argument('department', type=str)
teacher_args.add_argument('credits', type=int, help="Credits is required") 

teacher_fields = {
'id': fields.Integer,
'first_name': fields.String,
'last_name': fields.String,
'email': fields.String,
'phone': fields.String,
'department': fields.String,
'credits': fields.Integer,
'courses': fields.String,
'hire_date': fields.DateTime
}


class Teachers(Resource):
    @marshal_with(teacher_fields)
    def get(self):
        """Get all teachers
        ---
        tags:
            - Teachers
        summary: Retrieve all teachers
        description: This endpoint retrieves all teachers from the system.
        responses:
            200:
                description: List of all teachers retrieved successfully
                schema:
                    type: array
                    items:
                        type: object
                        properties:
                            id:
                                type: integer
                                description: The unique identifier of the teacher
                            first_name:
                                type: string
                                description: The first name of the teacher
                            last_name:
                                type: string
                                description: The last name of the teacher
                            email:
                                type: string
                                description: The email address of the teacher
                            phone:
                                type: string
                                description: The phone number of the teacher
                            department:
                                type: string
                                description: The department of the teacher
                            credits:
                                type: integer
                                description: The credits of the teacher
                            courses:
                                type: string
                                description: The courses taught by the teacher
                            hire_date:
                                type: string
                                format: date-time
                                description: The hire date of the teacher
            404:
                description: No teachers found
                schema:
                    type: object
                    properties:
                        message:
                            type: string
                            description: Teachers not found!
        """
        teachers = TeacherModel.query.all()
        if not teachers:
            abort(404, message="Teachers not found")
        return teachers
    
    @marshal_with(teacher_fields)
    def post(self):
        """Create a new teacher
        ---
        tags:
            - Teachers
        summary: Create a new teacher
        description: This endpoint creates a new teacher in the system.
        parameters:
            - in: body
              name: teacher
              description: Teacher data
              required: true
              schema:
                  type: object
                  required:
                      - first_name
                      - last_name
                      - email
                  properties:
                      first_name:
                          type: string
                          description: The first name of the teacher
                      last_name:
                          type: string
                          description: The last name of the teacher
                      email:
                          type: string
                          description: The email address of the teacher
                      phone:
                          type: string
                          description: The phone number of the teacher
                      department:
                          type: string
                          description: The department of the teacher
                      credits:
                          type: integer
                          description: The credits of the teacher
        responses:
            201:
                description: Teacher created successfully
                schema:
                    type: object
                    properties:
                        id:
                            type: integer
                            description: The unique identifier of the created teacher
                        first_name:
                            type: string
                            description: The first name of the teacher
                        last_name:
                            type: string
                            description: The last name of the teacher
                        email:
                            type: string
                            description: The email address of the teacher
                        phone:
                            type: string
                            description: The phone number of the teacher
                        department:
                            type: string
                            description: The department of the teacher
                        credits:
                            type: integer
                            description: The credits of the teacher
                        courses:
                            type: string
                            description: The courses taught by the teacher
                        hire_date:
                            type: string
                            format: date-time
                            description: The hire date of the teacher
            400:
                description: Bad request - validation error
                schema:
                    type: object
                    properties:
                        message:
                            type: string
                            description: Error message
        """
        args = teacher_args.parse_args()
        try:
            new_teacher = TeacherModel(
                first_name=args['first_name'],
                last_name=args['last_name'],
                email=args['email'],
                phone=args['phone'],
                department=args['department'],
                credits=args['credits'] 
                )
            db.session.add(new_teacher)
            db.session.commit()
            return new_teacher, 201
        
        except Exception as e:
            db.session.rollback()
            abort(400, message=f"Error creating as teacher{str(e)}")

class Teacher(Resource):
    @marshal_with(teacher_fields)
    def get(self, id):
        """Get a specific teacher by ID
        ---
        tags:
            - Teachers
        summary: Retrieve a teacher by ID
        description: This endpoint retrieves a specific teacher by their ID.
        parameters:
            - in: path
              name: id
              type: integer
              required: true
              description: The unique identifier of the teacher
        responses:
            200:
                description: Teacher retrieved successfully
                schema:
                    type: object
                    properties:
                        id:
                            type: integer
                            description: The unique identifier of the teacher
                        first_name:
                            type: string
                            description: The first name of the teacher
                        last_name:
                            type: string
                            description: The last name of the teacher
                        email:
                            type: string
                            description: The email address of the teacher
                        phone:
                            type: string
                            description: The phone number of the teacher
                        department:
                            type: string
                            description: The department of the teacher
                        credits:
                            type: integer
                            description: The credits of the teacher
                        courses:
                            type: string
                            description: The courses taught by the teacher
                        hire_date:
                            type: string
                            format: date-time
                            description: The hire date of the teacher
            404:
                description: Teacher not found
                schema:
                    type: object
                    properties:
                        message:
                            type: string
                            description: Teacher not found!
        """
        teacher = TeacherModel.query.filter_by(id=id).first()
        if not teacher:
            abort(404, message="Teacher not found")
        return teacher
    
    @marshal_with(teacher_fields)
    def patch(self, id=id):
        """Update a teacher by ID
        ---
        tags:
            - Teachers
        summary: Update a teacher
        description: This endpoint updates an existing teacher's information.
        parameters:
            - in: path
              name: id
              type: integer
              required: true
              description: The unique identifier of the teacher
            - in: body
              name: teacher
              description: Updated teacher data
              required: true
              schema:
                  type: object
                  required:
                      - first_name
                      - last_name
                      - email
                  properties:
                      first_name:
                          type: string
                          description: The first name of the teacher
                      last_name:
                          type: string
                          description: The last name of the teacher
                      email:
                          type: string
                          description: The email address of the teacher
                      phone:
                          type: string
                          description: The phone number of the teacher
                      department:
                          type: string
                          description: The department of the teacher
                      credits:
                          type: integer
                          description: The credits of the teacher
        responses:
            200:
                description: Teacher updated successfully
                schema:
                    type: object
                    properties:
                        id:
                            type: integer
                            description: The unique identifier of the teacher
                        first_name:
                            type: string
                            description: The first name of the teacher
                        last_name:
                            type: string
                            description: The last name of the teacher
                        email:
                            type: string
                            description: The email address of the teacher
                        phone:
                            type: string
                            description: The phone number of the teacher
                        department:
                            type: string
                            description: The department of the teacher
                        credits:
                            type: integer
                            description: The credits of the teacher
                        courses:
                            type: string
                            description: The courses taught by the teacher
                        hire_date:
                            type: string
                            format: date-time
                            description: The hire date of the teacher
            404:
                description: Teacher not found
                schema:
                    type: object
                    properties:
                        message:
                            type: string
                            description: Teacher not found!
            400:
                description: Bad request - validation error
                schema:
                    type: object
                    properties:
                        message:
                            type: string
                            description: Error message
        """
        args = teacher_args.parse_args()
        teacher = TeacherModel.query.filter_by(id=id).first()
        if not teacher:
            abort(404, message="Teacher not found")
        try:
            teacher.first_name = args['first_name']
            teacher.last_name = args['last_name']
            teacher.email = args['email']
            teacher.phone = args['phone']
            teacher.department = args['department']
            teacher.credits = args['credits'] 
            db.session.commit()
            return teacher, 200
        
        except Exception as e:
            db.session.rollback()
            abort(400, message=f"Error updating the teacher{str(e)}")
    
    @marshal_with(teacher_fields)
    def delete(self, id):
        """Delete a teacher by ID
        ---
        tags:
            - Teachers
        summary: Delete a teacher
        description: This endpoint deletes a teacher from the system.
        parameters:
            - in: path
              name: id
              type: integer
              required: true
              description: The unique identifier of the teacher
        responses:
            204:
                description: Teacher deleted successfully
            404:
                description: Teacher not found
                schema:
                    type: object
                    properties:
                        message:
                            type: string
                            description: Teacher not found!
            400:
                description: Bad request - error deleting teacher
                schema:
                    type: object
                    properties:
                        message:
                            type: string
                            description: Error message
        """
        teacher = TeacherModel.query.filter_by(id=id).first()
        if not teacher:
            abort(404, message="Teacher not found")
        try:
            db.session.delete(teacher)
            db.session.commit()
            return '', 204
        
        except Exception as e:
            db.session.rollback()
            abort(400, message=f"Error deleting the teacher{str(e)}")         
