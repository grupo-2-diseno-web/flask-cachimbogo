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
        
