from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models.tema import TemaModel
from schemas.tema import TemaSchema

tema_schema = TemaSchema()
temas_schema = TemaSchema(many=True)

class Tema(Resource):
    @jwt_required
    def get(self, id_asignatura):
        temas = TemaModel.todas_los_temas(id_asignatura)
        return {'data': temas_schema.dump(temas)}, 200
        
