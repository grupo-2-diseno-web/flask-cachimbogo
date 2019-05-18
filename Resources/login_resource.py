from flask_restful import Resource
from flask_restful import reqparse
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from Querys.login_query import user_exists, is_password
import Utils.constants as constants


class Login(Resource):

    def __init__(self):
        self.username = ""
        self.password = ""

    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str,
                                help='Username to authenticate')
            parser.add_argument('password', type=str,
                                help='Password to create user')
            args = parser.parse_args()

            self.username = args['username']
            self.password = args['password']

            if self.username and self.password:
                if user_exists(self.username) and is_password(self.username, self.password):
                    access_token = create_access_token(identity=self.username)
                    return {'access_token': access_token}, 200
                else:
                    return {'message': constants.WRONG_LOGIN}, 404
            else:
                return {'message': constants.FIELD_NULL}, 400

        except Exception as e:
            return {'error': str(e)}

    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return {'current_user': current_user}, 200
