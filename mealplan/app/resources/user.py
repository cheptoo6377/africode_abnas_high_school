from app.models.user import UserModel
from flask_restful import Resource, reqparse,abort,marshal_with,fields
from app import db


user_args = reqparse.RequestParser()
user_args.add_argument('username', type=str, required=True, help='Username cannot be blank')
user_args.add_argument('firstname', type=str, required=True, help='First name cannot be blank')
user_args.add_argument('lastname', type=str, required=True, help='Last name cannot be blank')
user_args.add_argument('password', type=str, required=True, help='Password cannot be blank')

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'firstname': fields.String,
    'lastname': fields.String
}

#resource for all users
class Users(Resource):
   @marshal_with(user_fields)
   #get all users
   def get(self):
      users = UserModel.query.all()
      if not users:
         abort(404,message='users not found')
      return users
   

   @marshal_with(user_fields)
   #create a user
   def post(self):
      args = user_args.parse_args()
      try:
         new_user = User(username=args['username'],
                        firstname=args['firstname'],
                        lastname=args['lastname'],
                        password=args['password'])
         db.session.add(new_user)
         db.session.commit()
          
      except Exception as e:
         db.session.rollback()
         abort(400, message='error')
      users = UserModel.query.all()
      return users
class User(Resource):
   @marshal_with(user_fields)
   def get(self,id):
      user = UserModel.query.filter_by(id=id).first()

      if not user:
         abort(404,message='user not found')
      return user
   

  
   @marshal_with(user_fields)
   def patch(self, id):
         args = user_args.parse_args()
         user = UserModel.query.filter_by(id=id).first()
         if not user:
            abort(404, message="User with that id not found")
         user.username = args["username"]
         user.firstname = args["firstname"]
         user.lastname = args["lastname"]
         user.password = args["password"]
         db.session.commit()
         return user 
   @marshal_with(user_fields)
   def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
           abort(404,message="cannot delete this user")
        db.session.delete(user)
        db.session.commit()
        return '', 204