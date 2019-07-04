from ma import ma
from models.pregunta import PreguntaModel

class PreguntaAleatoriaSchema(ma.ModelSchema):
    class Meta:
        model = PreguntaModel
        load_only = ("id_subtema", "subtema", "correcta_num", "id_tipopregunta", "tipo_pregunta", "dificultad", "informacion")
        include_fk = True