from Resources.default_resource import DefaultResource
from .asignatura_query import AsignaturaQuery
import Utils.messages_constants as mc


class Asignatura(DefaultResource):

    def __init__(self):
        self.query = AsignaturaQuery()
        super().__init__()

    def get(self):
        try:
            data = self.query.get_asignaturas()
            return {'data': data}, 200
        except Exception as e:
            return {'error': str(e)}, 500
