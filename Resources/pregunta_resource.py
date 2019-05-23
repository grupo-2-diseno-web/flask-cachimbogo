from flask_restful import Resource
from Querys.preguntas_query import get_random_questions
import Utils.constants as constants
from Utils.utils import build_response


class Pregunta(Resource):
    def get(self, id=None, completado=None):
        try:
            data = None
            if id is None and completado is None:
                data = get_random_questions(10,1)
            data_response = build_response(constants.PREGUNTA_COLUMN, data)
            return {'data': data_response}, 200
        except Exception as e:
            return {'error': str(e)}, 500
