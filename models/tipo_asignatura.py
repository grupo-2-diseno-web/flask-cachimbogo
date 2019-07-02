from db import db


class TipoAsignaturaModel(db.Model):
    __tablename__ = 'tipo_asignatura'

    id_tipo_asignatura = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(10), nullable=False)

    asignaturas = db.relationship('AsignaturaModel', lazy='dynamic')