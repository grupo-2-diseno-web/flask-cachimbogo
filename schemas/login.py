from ma import ma
from marshmallow import Schema, fields

class LoginSchema(Schema):
    usuario = fields.String(required=True)
    password = fields.String(required=True)
        