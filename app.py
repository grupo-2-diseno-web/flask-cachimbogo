from flask import Flask
from Routes.routes import init_api
from DB.connection import Connection
from flask_jwt_extended import JWTManager


app = Flask(__name__)
con = Connection()
con.init_database(app)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
app.config['BUNDLE_ERRORS'] = True
jwt = JWTManager(app)
init_api(app)


if __name__ == '__main__':
    app.run(debug=True, use_debugger=True,
            use_reloader=True)
