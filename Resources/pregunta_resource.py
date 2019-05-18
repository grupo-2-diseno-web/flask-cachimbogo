from flask_restful import Resource
from Querys.preguntas_query import get_id_pregunta, get_pregunta_by_id


class Pregunta(Resource):
    def get(self):
        return {'id_preguntas': get_pregunta_by_id(353)}, 200
