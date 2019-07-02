#from models.respuesta import RespuestaModel
from marshmallow import Schema, fields


class RespuestaSchema(Schema):
    id_usuario = fields.Int(required=True)
    id_pregunta = fields.Int(required=True)
    correcta_num = fields.Int(required=True)
    #class Meta:
    #    model = RespuestaModel
    #    load_only = ("acertada",)
