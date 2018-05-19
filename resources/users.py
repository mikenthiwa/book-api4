from flask_restplus import Api, Resource, reqparse
from flask import Blueprint
from app.models import Users




# Create blueprint for users.py resource
user_api = Blueprint('resources.users', __name__)
api = Api(user_api)

# instantiate users from class User in data.models

class Register(Resource):
    """Methods = [POST, GET]"""

    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True,
                        help="No username provided", location=['json'])

    parser.add_argument('email', required=True,
                        help="No email provided", location=['json'])

    parser.add_argument('password', required=True,
                        help="No password provided", location=['json'])



    def post(self):
        """register user
           endpoint = /api/v1/auth/register"""

        args = self.parser.parse_args()

        username = args['username']
        email = args['email']
        password = args['password']

        response = Users.create_user(username=username, email=email, password=password)
        return response


class Login(Resource):
    """method = [post]"""

    req_data = reqparse.RequestParser()
    req_data.add_argument('username', required=True,
                          help='username required', location=['json'])

    req_data.add_argument('password', required=True,
                          help='password required', location=['json'])

    def post(self):
        """login User
        endpoint = /api/v1/auth/login"""

        args = self.req_data.parse_args()
        username = args['username']
        password = args['password']
        response = Users.login_user(username=username, password=password)
        return response


api.add_resource(Register, '/auth/register', endpoint='register')
api.add_resource(Login, '/auth/login', endpoint='login')
