from db import db


class DificultadModel(db.Model):
    __tablename__ = 'dificultad'

    id_dificultad = db.Column(db.Integer, primary_key=True)
    nivel = db.Column(db.String(10), nullable=False)

    preguntas = db.relationship('PreguntaModel', backref='dificultad', lazy='dynamic')
