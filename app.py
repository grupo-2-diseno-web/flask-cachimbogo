from flask import Flask
from Routes.routes import ApiRest
from DB.connection import Connection
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from Utils.crypto import Crypto
import os
from config import Config
from db import db


app = Flask(__name__)
CORS(app)
con = Connection()
con.init_database(app)
crypto = Crypto(app)
#app.config['JWT_SECRET_KEY'] = 'super-secret'
#if 'ENV' in os.environ:
#    app.config['JWT_SECRET_KEY'] = os.environ['SECRET_KEY']  # Change this!
#app.config['BUNDLE_ERRORS'] = True
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)
api = ApiRest(app)
api.init_api()

if __name__ == '__main__':
    app.run(debug=True, use_debugger=True,
            use_reloader=True, host="0.0.0.0")
