from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from Utils.utils import set_params
import Resources.Login.params_constants as pc
import Utils.messages_constants as mc
from .login_query import LoginQuery


class Login(Resource):

    def __init__(self):
        self.query = LoginQuery()

    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            set_params(parser, pc.PARAMS,
                       pc.PARAMS_TYPE, pc.PARAMS_HELP)
            args = parser.parse_args()

            username = args['username']
            password = args['password']

            if username and password:
                if self.query.user_exists(username) and self.query.is_password(username, password):
                    access_token = create_access_token(identity=username)
                    response = self.query.select_usuario(username)[0]
                    response['access_token'] = access_token
                    return response, 200
                else:
                    return {'message': mc.WRONG_LOGIN}, 404
            else:
                return {'message': mc.FIELD_NULL}, 400

        except Exception as e:
            return {'error': str(e)}, 500

    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return {'current_user': current_user}, 200
