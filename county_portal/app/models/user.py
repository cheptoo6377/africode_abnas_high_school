from app.extension import db
from flask_security import UserMixin,RoleMixin
import uuid

#association table
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                       db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
                       )

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    #basic identity fields that comes with flask security
    id = db.Column(db.Integer, primary_key=True)
    
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    #account status
    active = db.Column(db.Boolean(),default=True)
   
    confirmed_at = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime(), default=db.func.current_timestamp())
    #flask security required for tokens,sessions,password
    fs_uniquifier = db.Column(db.String(200), nullable=False,unique=True,default=lambda:str(uuid.uuid4()))
    #tracking fields
    # TODO

    #roles
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    def __repr__(self):
        return f"<User {self.email} {self.roles}>"

    
    

class Role(db.Model,RoleMixin):
    __tablename__ = 'roles'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(150), nullable=False)

    
    
