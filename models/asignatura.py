from db import db


class AsignaturaModel(db.Model):
    __tablename__ = 'asignatura'

    id_asignatura = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    imagen = db.Column(db.String(200))

    id_tipo_asignatura = db.Column(db.Integer, db.ForeignKey('tipo_asignatura.id_tipo_asignatura'), nullable=False)
    temas = db.relationship('TemaModel', backref='asignatura', lazy='dynamic')
    
    @classmethod
    def todas_las_asignaturas(cls):
        return cls.query.all()