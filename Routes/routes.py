from flask_restful import Api
from Resources.login_resource import Login
from Resources.pregunta_resource import Pregunta


api = None


def init_api(app):
    api = Api(app)
    api.add_resource(Login, '/login')
    api.add_resource(Pregunta, '/pregunta/<int:id>/<int:completado>',
                     '/pregunta', '/pregunta/<int:id>')
