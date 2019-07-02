from db import db


class TipoPreguntaModel(db.Model):
    __tablename__ = 'tipo_pregunta'

    id_tipopregunta = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(10), nullable=False)

    preguntas = db.relationship('PreguntaModel', backref='tipo_pregunta', lazy='dynamic')