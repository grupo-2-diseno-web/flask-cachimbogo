from flask_restful import Resource
from .tema_query import TemaQuery
import Utils.messages_constants as mc


class Tema(Resource):

    def __init__(self):
        self.query = TemaQuery()

    def get(self, id_asignatura=None):
        try:
            if id_asignatura is not None:
                data = self.query.select_tema(id_asignatura)
                return {'data': data}, 200
            else:
                return {'error': mc.RESOURCE_NOT_FOUND}, 400
        except Exception as e:
            return {'error': str(e)}, 500
