from flask_restful import Resource, reqparse
from Querys.preguntas_query import get_random_questions, get_pregunta_by_subtema, get_pregunta_populate, insert_pregunta
import Utils.messages_constants as messages_constants
import Utils.params_constants as params_constants
from Utils.utils import set_params, get_params


class Pregunta(Resource):
    def get(self, id=None, completado=None, tipo=None):
        try:
            data = None
            if id is not None and completado is not None:
                data = get_random_questions(id, completado)
            elif id is not None and tipo is not None:
                data = get_pregunta_by_subtema(id)
            elif id is not None:
                data = get_pregunta_populate(id)
            else:
                return {'error': messages_constants.RESOURCE_NOT_FOUND}, 400
            return {'data': data}, 200
        except Exception as e:
            return {'error': str(e)}, 500

    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            set_params(parser, params_constants.PREGUNTA_PARAMS,
                       params_constants.PREGUNTA_PARAMS_TYPE, params_constants.PREGUNTA_PARAMS_HELP)
            args = parser.parse_args()

            params = get_params(args, params_constants.PREGUNTA_PARAMS)

            if insert_pregunta(params):
                return {'message': messages_constants.INSERT_SUCCESS}, 201
            else:
                return {'error': messages_constants.DB_ERROR}, 500

        except Exception as e:
            return {'error': str(e)}, 500
