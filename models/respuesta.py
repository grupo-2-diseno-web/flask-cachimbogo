from db import db


class RespuestaModel(db.Model):
    __tablename__ = 'respuesta'

    id_usuario = db.Column(db.Integer, primary_key=True)
    id_pregunta = db.Column(db.Integer, primary_key=True)
    acertada = db.Column(db.Integer)

    def __init__(self, id_usuario, id_pregunta, acertada):
        self.id_usuario = id_usuario
        self.id_pregunta = id_pregunta
        self.acertada = acertada

    @classmethod
    def existe_respuesta(cls, id_usuario, id_pregunta):
        return cls.query.filter_by(id_usuario=id_usuario, id_pregunta=id_pregunta).first()

    def guardar_en_la_bd(self):
        db.session.add(self)
        db.session.commit()