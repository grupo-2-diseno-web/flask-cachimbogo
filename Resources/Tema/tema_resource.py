from flask_restful import Resource
from models.tema import TemaModel
from schemas.tema import TemaSchema

tema_schema = TemaSchema()
temas_schema = TemaSchema(many=True)

class Tema(Resource):
    def get(self, id_asignatura=None):
        try:
            if id_asignatura is not None:
                temas = TemaModel.todas_los_temas(id_asignatura)
                return {'data': temas_schema.dump(temas)}, 200
            else:
                return {'error': mc.RESOURCE_NOT_FOUND}, 400
        except Exception as e:
            return {'error': str(e)}, 500
