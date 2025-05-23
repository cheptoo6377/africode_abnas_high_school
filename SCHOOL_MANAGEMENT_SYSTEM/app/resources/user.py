
from flask_restful import Resource,marshal_with,fields,abort,reqparse
from app.models.users import UserModel
from app.extension import db



#DATABASE MODEL

   
#request parser
user_args = reqparse.RequestParser()
user_args.add_argument('username', type=str, required=True, help='username cannot be empty')
user_args.add_argument('email', type=str, required=True, help='email cannot be empty')
user_args.add_argument('password', type=str, required=True, help='password cannot be empty')

#output fields
user_fields = {
   'id': fields.Integer,
   'username': fields.String,
   'email': fields.String,
   'password' : fields.String
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
         new_user = UserModel(username=args['username'], email=args['email'] , password=args['password'])
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
   

   # @marshal_with(user_fields)
   # def patch(self, id):
   #     args = user_args.parse_args()
   #     user = UserModel.query.filter_by(id=id).first()
   #     if not user:
   #      abort(404,message='no user with that id')
   #      user.username = args['username']
   #      user.email = args['email']
   #      db.session.commit()
   #      return user
   
   @marshal_with(user_fields)
   def patch(self, id):
         args = user_args.parse_args()
         user = UserModel.query.filter_by(id=id).first()
         if not user:
            abort(404, message="User with that id not found")
         user.username = args["username"]
         user.email = args["email"]
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
        
      

   








