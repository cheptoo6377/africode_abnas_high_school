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

    #profile
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone_number = db.Column(db.String(20), unique=True, nullable=True)


    #account status
    active = db.Column(db.Boolean(),default=True)
   
    confirmed_at = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime(), default=db.func.current_timestamp())
    #flask security required for tokens,sessions,password
    fs_uniquifier = db.Column(db.String(200), nullable=False,unique=True,default=lambda:str(uuid.uuid4()))
    
    county_id = db.Column(db.Integer, db.ForeignKey('counties.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id')) 


     # Foreign key to Department table
      # Foreign key to County table
    #tracking fields
    # TODO
    last_login_at = db.Column(db.DateTime)
    current_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String(50))
    current_login_ip = db.Column(db.String(50))
    login_count = db.Column(db.Integer, default=0)


    #roles
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    def __repr__(self):
        return f"<User {self.email} {self.roles}>"
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.email.split('@')[0] #fallback if no first name or last name
   
    def has_role(self, role_name):
        return any(role.name == role_name for role in self.roles) 
    

    
    

class Role(db.Model,RoleMixin):
    __tablename__ = 'roles'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<Role {self.name}>'
    
