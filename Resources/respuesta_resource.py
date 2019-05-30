from flask_restful import Resource, reqparse
import Utils.messages_constants as messages_constants
import Utils.params_constants as params_constants
from Querys.respuesta_query import check_answer
from Utils.utils import set_params, get_params


class Respuesta(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            set_params(parser, params_constants.RESPUESTA_PARAMS,
                       params_constants.RESPUESTA_PARAMS_TYPE, params_constants.RESPUESTA_PARAMS_HELP)
            args = parser.parse_args()

            params = get_params(args, params_constants.RESPUESTA_PARAMS)

            response = check_answer(params[0], params[1])

            return response, 200

        except Exception as e:
            return {'error': str(e)}, 500