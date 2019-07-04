from db import db


class UsuarioModel(db.Model):
    __tablename__ = 'usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    nombres = db.Column(db.String(80), nullable=False)
    apellidos = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(30), unique=True, nullable=False)
    monedas = db.Column(db.Integer)

    def guardar_en_la_bd(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def existe_usuario(cls, usuario, correo):
        return cls.query.filter(db.or_(cls.usuario==usuario, cls.correo==correo)).first()
    
    @classmethod
    def usuario_por(cls, usuario):
        return cls.query.filter_by(usuario=usuario).first()