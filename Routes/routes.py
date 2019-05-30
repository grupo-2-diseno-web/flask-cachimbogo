from flask_restful import Api
from Resources.login_resource import Login
from Resources.pregunta_resource import Pregunta
from Resources.usuario_resource import Usuario
from Resources.respuesta_resource import Respuesta
from Resources.usuario_asignatura_resource import UsuarioAsignatura
from Resources.tema_resource import Tema


api = None


def init_api(app):
    api = Api(app)
    api.add_resource(Login, '/login')
    api.add_resource(Pregunta, '/pregunta/<int:id>/<int:completado>',
                     '/pregunta', '/pregunta/<int:id>', '/pregunta/<string:tipo>/<int:id>')
    api.add_resource(Usuario, '/usuario')
    api.add_resource(Respuesta, '/respuesta')
    api.add_resource(UsuarioAsignatura, '/usuarioAsignatura')
    api.add_resource(Tema, '/temaAsignatura/<int:id_asignatura>')
