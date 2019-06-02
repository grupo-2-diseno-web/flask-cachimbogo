from flask_restful import Resource, reqparse
import Utils.messages_constants as mc
import Resources.Usuario.params_constants as pc
from Utils.utils import set_params, get_params
from .usuario_query import insert_usuario


class Usuario(Resource):

    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            set_params(parser, pc.PARAMS,
                       pc.PARAMS_TYPE, pc.PARAMS_HELP)
            args = parser.parse_args()

            params = get_params(args, pc.PARAMS)

            if insert_usuario(params):
                return {'message': mc.INSERT_SUCCESS}, 201
            else:
                return {'error': mc.DB_ERROR}, 500

        except Exception as e:
            return {'error': str(e)}, 500
