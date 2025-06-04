from flask import Flask
from flask_security import SQLAlchemyUserDatastore,hash_password
from app.extension import db,migrate,mail,security
from app.main.views import main_bp
from app.api.routes import api_bp
from app.auth.routes import auth_bp
from config import Config
from app.models.user import User,Role
from app.models.county import County,Department
from app.forms import ExtendedLoginForm,ExtendedRegisterForm
import uuid


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)








    #register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)
    
    #custom user registration handler
    from flask_security.signals import user_registered
    @user_registered.connect_via(app)
    def user_registered_sighandler(sender, user, confirm_token, **extra):     
        """Handle post-registration logic"""                                  
        # Assign default 'Citizen' role                                       
        default_role = Role.query.filter_by(name='Citizen').first()           
        if default_role and not user.roles:                                   
            user.roles.append(default_role)                                   
            db.session.commit()                                               
                                                                                
        print(f"New user registered: {user.email} in {user.county.name if user.county else 'No County'}")

    #import models
    user_datastore = SQLAlchemyUserDatastore(db,User,Role)
    security.init_app(app,user_datastore,register_form=ExtendedRegisterForm,login_form=ExtendedLoginForm)
    

    with app.app_context():
        db.create_all()
        

        # Create sample counties                                                  
        counties_data = [                                                         
            {'name': 'Bomet County', 'code': '036', 'description': 'Kipsisgis County'},                                                                       
            {'name': 'Narok County', 'code': '033', 'description': 'Maa county'},                                                                       
            {'name': 'Kericho County', 'code': '035', 'description': 'Green county'},                                                                       
        ]
       
        created_counties = []
        for county_data in counties_data:
            county = County.query.filter_by(name=county_data['name']).first()
            if not county:
                county = County(**county_data)
                db.session.add(county)
                created_counties.append(county)
            else:
                created_counties.append(county)
        db.session.commit()
        

        # Create sample departments for each county
    
        departments_data = [
            {'name': 'Trade & Commerce', 'code': 'TC'},
            {'name': 'Lands & Housing', 'code': 'LH'},
            {'name': 'Health Services', 'code': 'HS'},
            {'name': 'Environment & Water', 'code': 'EW'},
        ]
 

        for county in created_counties:
         for dept_data in departments_data:
          department = Department.query.filter_by(name=dept_data['name'], county_id=county.id).first()
        if not department:
            department = Department(name=dept_data['name'], code=dept_data['code'], county_id=county.id)
            db.session.add(department)
        db.session.commit()
# ...existing code...
        roles_data = [
            {'name': 'super_admin', 'description': 'Administrator role'},
            {'name': 'staff', 'description': 'Regular staff role'},
            {'name': 'citizen', 'description': 'Citizen role'},
            {'name': 'guest', 'description': 'Guest role'}
        ]
        for role_data in roles_data:
            role = Role.query.filter_by(name=role_data['name']).first()
            if not role:
                role = Role(**role_data)
                db.session.add(role)
            admin_role = Role.query.filter_by(name='super_admin').first()
            admin_user = User.query.filter_by(email='cheptoodorothy69@example.com').first()
            if not admin_role:
                admin_role = Role(name='super_admin', description='Administrator role')
                db.session.add(admin_role)
            if not admin_user:
                admin_user = User(email='cheptoodorothy69@example.com', 
                                  first_name = 'deom',last_name = 'cysry',
                                  county_id = 34,
                                  password=hash_password('@Cheptoo6377'),
                                  active=True,roles=[admin_role],
                                  fs_uniquifier=str(uuid.uuid4()))
                db.session.add(admin_user)
                db.session.commit()
                print("Admin user created with email:", admin_user.email)


            staff_role = Role.query.filter_by(name='staff').first()
            new_staff = User.query.filter_by(email='vcctgk@gmail.com').first()

            if not staff_role:
                staff_role = Role(name='staff', description='Regular staff role')
                db.session.add(staff_role)
            if not new_staff:
                new_staff = User(email='vcctgk@gmail.com', password=hash_password('My1234567'), active=True, roles=[staff_role], fs_uniquifier=str(uuid.uuid4()))
                db.session.add(new_staff)
            db.session.commit()
            print("Staff user created with email:", new_staff.email)


            citizen_role = Role.query.filter_by(name='citizen').first()
            new_citizen = User.query.filter_by(email='cheppy@gmail.com').first()
            if not citizen_role:
                citizen_role = Role(name='citizen', description='Citizen role')
                db.session.add(citizen_role)
            if not new_citizen:
                new_citizen = User(email='cheppy@gmail.com', password=hash_password('My1234568'), active=True, roles=[citizen_role], fs_uniquifier=str(uuid.uuid4()))
                db.session.add(new_citizen)
            db.session.commit()
            print("Citizen user created with email:", new_citizen.email)
            guest_role = Role.query.filter_by(name='guest').first()
            new_guest = User.query.filter_by(email='guesty@example.com').first()
            if not guest_role:
                guest_role = Role(name='guest', description='Guest role')
                db.session.add(guest_role)
            if not new_guest:
                new_guest = User(email='guesty@example.com', password=hash_password('My1234569'), active=True, roles=[guest_role], fs_uniquifier=str(uuid.uuid4()))
                db.session.add(new_guest)
        

        

    return app