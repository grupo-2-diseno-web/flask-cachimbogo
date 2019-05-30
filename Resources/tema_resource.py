from flask_restful import Resource
from Querys.tema_query import select_tema
import Utils.messages_constants as messages_constants


class Tema(Resource):
    def get(self, id_asignatura=None):
        try:
            if id_asignatura is not None:
                data = select_tema(id_asignatura)
                return {'data': data}, 200
            else:
                return {'error': messages_constants.RESOURCE_NOT_FOUND}, 400
        except Exception as e:
            return {'error': str(e)}, 500
