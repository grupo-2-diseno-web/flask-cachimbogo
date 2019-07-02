from flask_restful import Resource
from models.subtema import SubTemaModel
from schemas.subtema import SubTemaSchema

subtema_schema = SubTemaSchema()
subtemas_schema = SubTemaSchema(many=True)


class Subtema(Resource):

    def get(self, id_tema=None):
        try:
            if id_tema is not None:
                subtemas = SubTemaModel.todos_los_subtemas(id_tema)
                return {'data': subtemas_schema.dump(subtemas)}, 200
            else:
                return {'error': mc.RESOURCE_NOT_FOUND}, 400
        except Exception as e:
            return {'error': str(e)}, 500
