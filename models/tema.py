from db import db


class TemaModel(db.Model):
    __tablename__ = 'tema'

    id_tema = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    id_asignatura = db.Column(db.Integer, db.ForeignKey('asignatura.id_asignatura'), nullable=False)
    subtemas = db.relationship('SubTemaModel', backref='tema', lazy='dynamic')
    
    @classmethod
    def todas_los_temas(cls, id_asignatura):
        return cls.query.filter_by(id_asignatura=id_asignatura)