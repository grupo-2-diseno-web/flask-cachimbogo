from ma import ma
from models.subtema import SubTemaModel
from schemas.tema import TemaSchema

class SubTemaSchema(ma.ModelSchema):
    tema = ma.Nested(TemaSchema)

    class Meta:
        model = SubTemaModel
        fields = ("id_subtema", "nombre", "tema")