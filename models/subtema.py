from db import db
#from models import pregunta


class SubTemaModel(db.Model):
    __tablename__ = 'subtema'

    id_subtema = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    id_tema = db.Column(db.Integer, db.ForeignKey('tema.id_tema'), nullable=False)
    preguntas = db.relationship('PreguntaModel', backref='subtema', lazy='dynamic')

    def json(self):
        return {
            'id_subtema': self.id_subtema,
            'nombre': self.nombre
        }
    
    @classmethod
    def todos_los_subtemas(cls, id_tema):
        return cls.query.filter_by(id_tema=id_tema)