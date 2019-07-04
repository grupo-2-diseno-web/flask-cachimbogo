from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models.subtema import SubTemaModel
from schemas.subtema import SubTemaSchema

subtema_schema = SubTemaSchema()
subtemas_schema = SubTemaSchema(many=True)


class Subtema(Resource):
    @classmethod
    @jwt_required
    def get(cls, id_tema):
        subtemas = SubTemaModel.todos_los_subtemas(id_tema)
        return {'data': subtemas_schema.dump(subtemas)}, 200

