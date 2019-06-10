from Resources.default_resource import DefaultResource
from .usuario_asignatura_query import UsuarioAsignaturaQuery


class UsuarioAsignatura(DefaultResource):

    def __init__(self):
        self.query = UsuarioAsignaturaQuery()

    def get(self):
        try:
            parser = self.get_paser()
            parser.add_argument('id_usuario', type=int, location='args')
            args = parser.parse_args()
            data = self.query.select_usuario_asignatura(args['id_usuario'])
            return {'data': data}, 200
        except Exception as e:
            return {'error': str(e)}, 500
