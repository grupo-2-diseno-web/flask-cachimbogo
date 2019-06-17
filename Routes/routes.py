from flask_restful import Api
from Resources.Login.login_resource import Login
from Resources.Pregunta.pregunta_resource import Pregunta
from Resources.Usuario.usuario_resource import Usuario
from Resources.Respuesta.respuesta_resource import Respuesta
from Resources.UsuarioAsignatura.usuario_asignatura_resource import UsuarioAsignatura
from Resources.UsuarioTema.usuario_tema_resource import UsuarioTema
from Resources.Subtema.subtema_resource import Subtema
from Resources.UsuarioSubtema.usuario_subtema_resource import UsuarioSubtema


class ApiRest(object):

    def __init__(self, app):
        self.api = Api(app)

    def init_api(self):
        self.api.add_resource(Login, '/login')
        self.api.add_resource(Pregunta, '/pregunta/<int:id>/<int:completado>',
                              '/pregunta', '/pregunta/<int:id>', '/pregunta/<string:tipo>/<int:id>')
        self.api.add_resource(Usuario, '/usuario')
        self.api.add_resource(Respuesta, '/respuesta')
        self.api.add_resource(UsuarioAsignatura, '/usuarioAsignatura')
        self.api.add_resource(
            UsuarioTema, '/temaAsignatura')
        self.api.add_resource(Subtema, '/subtemaTema/<int:id_tema>')
        self.api.add_resource(UsuarioSubtema, '/usuarioSubtema')
