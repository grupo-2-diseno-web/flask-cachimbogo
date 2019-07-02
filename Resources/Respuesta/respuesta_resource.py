"""from Resources.default_resource import DefaultResource
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

            response = self.query.check_answer(args)

            return response

        except Exception as e:
            return {'error': str(e)}, 500
"""
from flask_restful import Resource
from flask import request
from models.pregunta import PreguntaModel
from models.respuesta import RespuestaModel
from schemas.respuesta import RespuestaSchema

respuesta_schema = RespuestaSchema()


class Respuesta(Resource):
    def post(self):
        respuesta_json = request.get_json()
        respuesta = respuesta_schema.load(respuesta_json)
        pregunta = PreguntaModel.pregunta_por_id(respuesta["id_pregunta"])
        acertada = pregunta.correcta_num == respuesta["correcta_num"]
        if not RespuestaModel.existe_respuesta(respuesta_json["id_usuario"], respuesta_json["id_pregunta"]):
            respuesta = RespuestaModel(respuesta_json["id_usuario"], respuesta_json["id_pregunta"], acertada)
            respuesta.guardar_en_la_bd()
            return {"data": {"acertada": acertada, "informacion": pregunta.informacion}}
        return {"mensaje": "Ya has respondido la pregunta"}
        
