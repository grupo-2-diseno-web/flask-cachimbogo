from flask_restful import Resource, reqparse
import Resources.Respuesta.params_constants as pc
from .respuesta_query import RespuestaQuery
from Utils.utils import set_params, get_params


class Respuesta(Resource):

    def __init__(self):
        self.query = RespuestaQuery()

    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            set_params(parser, pc.PARAMS,
                       pc.PARAMS_TYPE, pc.PARAMS_HELP)
            args = parser.parse_args()

            params = get_params(args, pc.PARAMS)

            response = self.query.check_answer(params[0], params[1])

            return response, 200

        except Exception as e:
            return {'error': str(e)}, 500