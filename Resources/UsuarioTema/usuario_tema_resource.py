from Resources.default_resource import DefaultResource
from .usuario_tema_query import UsuarioTemaQuery


class UsuarioTema(DefaultResource):

    def __init__(self):
        self.query = UsuarioTemaQuery()

    def get(self):
        try:
            parser = self.get_paser()
            parser.add_argument('id_asignatura', type=int, location='args')
            parser.add_argument('id_usuario', type=int, location='args')
            args = parser.parse_args()
            data = self.query.select_usuario_tema(
                args['id_usuario'], args['id_asignatura'])
            return {'data': data}, 200
        except Exception as e:
            return {'error': str(e)}, 500
