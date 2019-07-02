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
