from flask_restful import Resource
from Querys.subtema_query import select_subtema
import Utils.messages_constants as mc


class Subtema(Resource):
    def get(self, id_tema=None):
        try:
            if id_tema is not None:
                data = select_subtema(id_tema)
                return {'data': data}, 200
            else:
                return {'error': mc.RESOURCE_NOT_FOUND}, 400
        except Exception as e:
            return {'error': str(e)}, 500
