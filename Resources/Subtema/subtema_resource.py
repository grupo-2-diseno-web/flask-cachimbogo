from flask_restful import Resource
from .subtema_query import SubtemaQuery
import Utils.messages_constants as mc


class Subtema(Resource):

    def __init__(self, *args, **kwargs):
        self.query = SubtemaQuery()

    def get(self, id_tema=None):
        try:
            if id_tema is not None:
                data = self.query.select_subtema(id_tema)
                return {'data': data}, 200
            else:
                return {'error': mc.RESOURCE_NOT_FOUND}, 400
        except Exception as e:
            return {'error': str(e)}, 500
