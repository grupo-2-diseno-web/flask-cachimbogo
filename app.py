from flask import Flask, jsonify
from Routes.routes import ApiRest
from DB.connection import Connection
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from Utils.crypto import Crypto
import os
from config import Config
from marshmallow import ValidationError
from ma import ma
from db import db


app = Flask(__name__)
CORS(app)
con = Connection()
con.init_database(app)
crypto = Crypto(app)
app.config.from_object(Config)
db.init_app(app)
ma.init_app(app)
jwt = JWTManager(app)
api = ApiRest(app)
api.init_api()

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400

if __name__ == '__main__':
    app.run(debug=True, use_debugger=True,
            use_reloader=True, host="0.0.0.0")
