from Resources.default_resource import DefaultResource
import Resources.UsuarioSubtema.params_constants as pc
from .usuario_subtema_query import UsuarioSubtemaQuery


class UsuarioSubtema(DefaultResource):

    def __init__(self):
        self.query = UsuarioSubtemaQuery()
        super().__init__()

    def post(self):
        try:
            # Parse the arguments
            self.set_params(pc.PARAMS,
                            pc.PARAMS_TYPE, pc.PARAMS_HELP)
            args = self.get_params(pc.PARAMS)

            response = self.query.check_answer(args)

            return response

        except Exception as e:
            return {'error': str(e)}, 500
