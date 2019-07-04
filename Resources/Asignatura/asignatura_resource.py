from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models.asignatura import AsignaturaModel
from schemas.asignatura import AsignaturaSchema

asignatura_schema = AsignaturaSchema()
asignatura_list_schema = AsignaturaSchema(many=True)

class Asignatura(Resource):
    @classmethod
    @jwt_required
    def get(cls):
        asignaturas = AsignaturaModel.todas_las_asignaturas()
        return {'data': asignatura_list_schema.dump(asignaturas)}, 200
