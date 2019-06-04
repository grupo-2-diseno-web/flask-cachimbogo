from flask_restful import Resource, reqparse
from .usuario_asignatura_query import UsuarioAsignaturaQuery


class UsuarioAsignatura(Resource):

    def __init__(self, *args, **kwargs):
        self.query = UsuarioAsignaturaQuery()

    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id_usuario', type=int, location='args')
            args = parser.parse_args()
            data = self.query.select_usuario_asignatura(args['id_usuario'])
            return {'data': data}, 200
        except Exception as e:
            return {'error': str(e)}, 500
