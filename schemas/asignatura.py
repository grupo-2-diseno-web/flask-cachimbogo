from ma import ma
from models.asignatura import AsignaturaModel


class AsignaturaSchema(ma.ModelSchema):
    class Meta:
        model = AsignaturaModel
        fields = ("id_asignatura", "nombre")