from Resources.default_resource import DefaultResource
import Utils.messages_constants as mc
import Resources.Usuario.params_constants as pc
from Utils.utils import set_params, get_params
from .usuario_query import UsuarioQuery


class Usuario(DefaultResource):

    def __init__(self):
        self.query = UsuarioQuery()
        super().__init__()

    def post(self):
        try:
            # Parse the arguments
            self.set_params(pc.PARAMS,
                       pc.PARAMS_TYPE, pc.PARAMS_HELP)

            params = self.get_params(pc.PARAMS)

            if self.query.insert_usuario(params):
                return {'message': mc.INSERT_SUCCESS}, 201
            else:
                return {'error': mc.DB_ERROR}, 500

        except Exception as e:
            return {'error': str(e)}, 500
