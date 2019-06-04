from flask_restful import Resource, reqparse
from .preguntas_query import PreguntaQuery
import Utils.messages_constants as mc
import Resources.Pregunta.params_constants as pc
from Utils.utils import set_params, get_params


class Pregunta(Resource):

    def __init__(self):
        self.query = PreguntaQuery()

    def get(self, id=None, completado=None, tipo=None):
        try:
            data = None
            if id is not None and completado is not None:
                data = self.query.get_random_questions(id, completado)
            elif id is not None and tipo is not None:
                data = self.query.get_pregunta_by_subtema(id)
            elif id is not None:
                data = self.query.get_pregunta_populate(id)
            else:
                return {'error': mc.RESOURCE_NOT_FOUND}, 400
            return {'data': data}, 200
        except Exception as e:
            return {'error': str(e)}, 500

    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            set_params(parser, pc.PARAMS,
                       pc.PARAMS_TYPE, pc.PARAMS_HELP)
            args = parser.parse_args()

            params = get_params(args, pc.PARAMS)

            if self.query.insert_pregunta(params):
                return {'message': mc.INSERT_SUCCESS}, 201
            else:
                return {'error': mc.DB_ERROR}, 500

        except Exception as e:
            return {'error': str(e)}, 500
