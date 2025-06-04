from flask import Blueprint

api_bp = Blueprint('api', __name__,url_prefix='/api')


@api_bp.route('/users', methods=['GET'])

def users_list():
    return [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]

