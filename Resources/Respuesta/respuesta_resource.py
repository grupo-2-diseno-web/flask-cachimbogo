from Resources.default_resource import DefaultResource
import Resources.Respuesta.params_constants as pc
from .respuesta_query import RespuestaQuery
from Utils.utils import set_params, get_params


class Respuesta(DefaultResource):

    def __init__(self):
        self.query = RespuestaQuery()
        super().__init__()

    def post(self):
        try:
            # Parse the arguments
            self.set_params(pc.PARAMS,
                            pc.PARAMS_TYPE, pc.PARAMS_HELP)
            args = self.get_params(pc.PARAMS)

            response = self.query.check_answer(args[0], args[1], args[2])

            return response, 200

        except Exception as e:
            return {'error': str(e)}, 500
