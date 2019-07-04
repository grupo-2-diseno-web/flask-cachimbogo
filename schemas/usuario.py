from ma import ma
from models.usuario import UsuarioModel


class UsuarioSchema(ma.ModelSchema):
    

    class Meta:
        model = UsuarioModel
        