from ma import ma
from models.tema import TemaModel
from schemas.asignatura import AsignaturaSchema

class TemaSchema(ma.ModelSchema):
    asignatura = ma.Nested(AsignaturaSchema)

    class Meta:
        model = TemaModel
        fields = ("id_tema", "nombre", "asignatura")