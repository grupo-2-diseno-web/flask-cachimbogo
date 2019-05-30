from flask_restful import Resource, reqparse
from Querys.usuario_asignatura_query import select_usuario_asignatura


class UsuarioAsignatura(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id_usuario', type=int, location='args')
            args = parser.parse_args()
            data = select_usuario_asignatura(args['id_usuario'])
            return {'data': data}, 200
        except Exception as e:
            return {'error': str(e)}, 500
