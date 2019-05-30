from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from Querys.login_query import user_exists, is_password
from Querys.usuario_query import select_usuario
from Utils.utils import set_params
import Utils.params_constants as params_constants
import Utils.messages_constants as messages_constants


class Login(Resource):

    def __init__(self):
        self.username = ""
        self.password = ""

    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            set_params(parser, params_constants.LOGIN_PARAMS,
                       params_constants.LOGIN_PARAMS_TYPE, params_constants.LOGIN_PARAMS_HELP)
            args = parser.parse_args()

            self.username = args['username']
            self.password = args['password']

            if self.username and self.password:
                if user_exists(self.username) and is_password(self.username, self.password):
                    access_token = create_access_token(identity=self.username)
                    response = select_usuario(self.username)
                    response['access_token'] = access_token
                    return response, 200
                else:
                    return {'message': messages_constants.WRONG_LOGIN}, 404
            else:
                return {'message': messages_constants.FIELD_NULL}, 400

        except Exception as e:
            return {'error': str(e)}, 500

    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return {'current_user': current_user}, 200
