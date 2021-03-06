from Resources.default_resource import DefaultResource
from .subtema_query import SubtemaQuery
import Utils.messages_constants as mc


class Subtema(DefaultResource):

    def __init__(self):
        self.query = SubtemaQuery()
        super().__init__()

    def get(self, id_tema=None):
        try:
            if id_tema is not None:
                data = self.query.get_subtemas(id_tema)
                return {'data': data}, 200
            else:
                return {'error': mc.RESOURCE_NOT_FOUND}, 400
        except Exception as e:
            return {'error': str(e)}, 500
