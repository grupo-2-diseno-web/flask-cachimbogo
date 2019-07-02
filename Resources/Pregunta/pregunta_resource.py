"""from Resources.default_resource import DefaultResource
from .pregunta_query import PreguntaQuery
import Utils.messages_constants as mc
import Resources.Pregunta.params_constants as pc
from Utils.utils import set_params, get_params


class Pregunta(DefaultResource):

    def __init__(self):
        self.query = PreguntaQuery()
        super().__init__()

    def get(self, id=None, completado=None, tipo=None):
        try:
            data = None
            if id is not None and completado is not None:
                data = self.query.get_random_questions(id, completado)
            elif id is not None and tipo is not None:
                data = self.query.get_pregunta_by_subtema(id)
            elif id is not None:
                data = self.query.get_pregunta_populate(id)
            else:
                return {'error': mc.RESOURCE_NOT_FOUND}, 400
            return {'data': data}, 200
        except Exception as e:
            return {'error': str(e)}, 500

    def post(self):
        try:
            # Parse the arguments
            self.set_params(pc.PARAMS,
                            pc.PARAMS_TYPE, pc.PARAMS_HELP)

            args = self.get_params(pc.PARAMS)

            if self.query.insert_pregunta(args):
                return {'message': mc.INSERT_SUCCESS}, 201
            else:
                return {'error': mc.DB_ERROR}, 500

        except Exception as e:
            return {'error': str(e)}, 500
"""
from flask_restful import Resource
from flask import request
from models.pregunta import PreguntaModel
from schemas.pregunta import PreguntaSchema
from schemas.aleatorio import PreguntaAleatoriaSchema

pregunta_schema = PreguntaSchema()
preguntas_schema = PreguntaSchema(many=True)
aleatorias_schema = PreguntaAleatoriaSchema(many=True)


class Pregunta(Resource):
    def get(self, id):
        pregunta = PreguntaModel.pregunta_por_id(id)
        return {'data': pregunta_schema.dump(pregunta)}

class ListaDePreguntasAleatorias(Resource):
    def get(self, id_subtema, completado):
        preguntas = PreguntaModel.preguntas_aleatorias(id_subtema, completado)
        return {'data': aleatorias_schema.dump(preguntas)}

class ListaDePreguntas(Resource):
    def get(self):
        preguntas = PreguntaModel.todas_las_preguntas()
        return {'data': preguntas_schema.dump(preguntas)}
    
    def post(self):
        pregunta_json = request.get_json()
        pregunta = pregunta_schema.load(pregunta_json)
        pregunta.guardar_en_la_bd()
        return pregunta_schema.dump(pregunta), 201
