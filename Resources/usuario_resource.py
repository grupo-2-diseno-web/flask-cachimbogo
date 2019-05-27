from flask_restful import Resource, reqparse
import Utils.messages_constants as messages_constants
import Utils.params_constants as params_constants
from Utils.utils import set_params, get_params
from Querys.usuario_query import insert_usuario


class Usuario(Resource):

    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            set_params(parser, params_constants.USUARIO_PARAMS,
                       params_constants.USUARIO_PARAMS_TYPE, params_constants.USUARIO_PARAMS_HELP)
            args = parser.parse_args()

            params = get_params(args, params_constants.USUARIO_PARAMS)

            if insert_usuario(params):
                return {'message': messages_constants.INSERT_SUCCESS}, 201
            else:
                return {'error': messages_constants.DB_ERROR}, 500

        except Exception as e:
            return {'error': str(e)}, 500
