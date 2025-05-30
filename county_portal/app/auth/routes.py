from flask import Blueprint
from flask_security import login_required,current_user,roles_required
from  app.models.user import User



auth_bp = Blueprint('auth', __name__,url_prefix='/auth')




@auth_bp.route('/profile')
@login_required
def profile():

    return{
        "message": "Welcome to your profile!",
        "user": {
            "id": current_user.id,
            "email": current_user.email,
           "active": current_user.active,
            
        }
    }

@auth_bp.route('/logout')
@login_required
def logout():
    return {
        "message": "You have been logged out successfully!"
    }
@auth_bp.route('/users', methods=['GET'])
@roles_required('super_admin')
@login_required
def get_users():
    users = User.query.all()
    return {
        "users": [
            {
                "id": user.id,
                "email": user.email,
                "active": user.active,
                "roles": [role.name for role in user.roles]
            }
            for user in users
        ]
    }
