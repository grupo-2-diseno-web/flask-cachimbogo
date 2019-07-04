from ma import ma
from models.pregunta import PreguntaModel
from models.dificultad import DificultadModel
from models.tipo_pregunta import TipoPreguntaModel
from schemas.subtema import SubTemaSchema

class PreguntaSchema(ma.ModelSchema):
    subtema = ma.Nested(SubTemaSchema)
    #clave1 = fields.String(required=True, error_messages={'required': "clave1 es requerido"})
    class Meta:
        model = PreguntaModel
        load_only = ("id_subtema",)
        dump_only = ("id_pregunta", "subtema")
        include_fk = True
