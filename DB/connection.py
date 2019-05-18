from flaskext.mysql import MySQL
from Utils.utils import get_config


class Connection(object):

    mysql = None

    def __init__(self):
        pass

    def init_database(self, app):
        Connection.mysql = MySQL()
        config_parser = get_config()
        app.config['MYSQL_DATABASE_USER'] = config_parser.get('config', 'user')
        app.config['MYSQL_DATABASE_PASSWORD'] = config_parser.get(
            'config', 'password')
        app.config['MYSQL_DATABASE_DB'] = config_parser.get('config', 'bd')
        app.config['MYSQL_DATABASE_HOST'] = config_parser.get('config', 'host')
        Connection.mysql.init_app(app)
