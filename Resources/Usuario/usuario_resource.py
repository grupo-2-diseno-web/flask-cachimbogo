from flask_restful import Resource
import Utils.messages_constants as mc
from Utils.crypto import Crypto
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token, get_raw_jwt, get_jwt_identity, jwt_required
from models.usuario import UsuarioModel
from schemas.usuario import UsuarioSchema
from schemas.login import LoginSchema
from blacklist import BLACKLIST

usuario_schema = UsuarioSchema()
login_schema = LoginSchema()

class Usuario(Resource):
    @classmethod
    def post(cls):
        usuario_json = request.get_json()
        usuario = usuario_schema.load(usuario_json)
        usuario.password = Crypto.get_crypto(usuario.password)

        if UsuarioModel.existe_usuario(usuario.usuario, usuario.correo):
            return {'message': mc.USER_ALREADY_EXISTS}, 400
        usuario.guardar_en_la_bd()
        return usuario_schema.dump(usuario), 201


class UsuarioLogin(Resource):
    @classmethod
    def post(cls):
        usuario_json = request.get_json()
        usuario_data = login_schema.load(usuario_json)
        usuario = UsuarioModel.existe_usuario(usuario_data["usuario"], "")
        
        if usuario and Crypto.check_crypto(usuario.password, usuario_data["password"]):
            access_token = create_access_token(identity=usuario.id_usuario, fresh=True)
            refresh_token = create_refresh_token(usuario.id_usuario)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        return {'message': mc.WRONG_LOGIN}


class UsuarioLogout(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        jti = get_raw_jwt()['jti'] # jti is "JWT ID", a unique identifier for a JWT.
        BLACKLIST.add(jti)
        return {'message': 'Sesión cerrada exitosamente'}, 200