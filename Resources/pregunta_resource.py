from flask_restful import Resource
from Querys.preguntas_query import get_id_pregunta, get_pregunta_by_id
import Utils.constants as constants
from Utils.utils import build_response


class Pregunta(Resource):
    def get(self):
        data = get_pregunta_by_id(353)
        data_response = build_response(constants.PREGUNTA_COLUMN, data)
        return {'data': data_response}, 200
