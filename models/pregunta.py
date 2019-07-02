from db import db
import random


class PreguntaModel(db.Model):
    __tablename__ = 'pregunta'

    id_pregunta = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(1000), nullable=False)
    clave1 = db.Column(db.String(200), nullable=False)
    clave2 = db.Column(db.String(200), nullable=False)
    clave3 = db.Column(db.String(200), nullable=False)
    clave4 = db.Column(db.String(200), nullable=False)
    clave5 = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.Integer)
    correcta_num = db.Column(db.Integer)
    informacion = db.Column(db.String(800))

    id_subtema = db.Column(db.Integer, db.ForeignKey('subtema.id_subtema'), nullable=False)
    id_tipopregunta = db.Column(db.Integer, db.ForeignKey('tipo_pregunta.id_tipopregunta'), nullable=False)
    id_dificultad = db.Column(db.Integer, db.ForeignKey('dificultad.id_dificultad'), nullable=False)
    
    @classmethod
    def todas_las_preguntas(cls):
        return cls.query.all()
    
    @classmethod
    def pregunta_por_id(cls, id_pregunta):
        return cls.query.get(id_pregunta)

    @classmethod
    def preguntas_aleatorias(cls, id_subtema ,completo):
        preguntas = cls.query.with_entities(cls.id_pregunta).filter_by(id_subtema=id_subtema) # obtener los ids de las preguntas del subtema
        ids = [pregunta[0] for pregunta in preguntas] # pasar de la lista de tuplas a una lista de solo enteros(ids)
        random.shuffle(ids) # remover para generar aleatoriedad
        if completo == 0:
            return cls.query.filter(cls.id_pregunta.in_(ids[:10]))
        return cls.query.filter(cls.id_pregunta.in_(ids[:7]))
    
    @classmethod
    def es_la_respuesta(cls, id_pregunta, correcta_num):
        pregunta = cls.query.with_entities(cls.correcta_num).filter_by(id_pregunta=id_pregunta).first()
        return pregunta[0] == correcta_num

    def guardar_en_la_bd(self):
        db.session.add(self)
        db.session.commit()
        
        
