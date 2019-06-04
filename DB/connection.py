from DB.mysql import MySQL
from Utils.utils import get_config
import configparser
import os


class Connection(object):

    mysql = None

    def __init__(self):
        Connection.mysql = MySQL()

    def init_database(self, app):
        if 'ENV' not in os.environ:
            config_parser = self.get_config()
            app.config['MYSQL_DATABASE_USER'] = config_parser.get(
                'config', 'user')
            app.config['MYSQL_DATABASE_PASSWORD'] = config_parser.get(
                'config', 'password')
            app.config['MYSQL_DATABASE_DB'] = config_parser.get('config', 'bd')
            app.config['MYSQL_DATABASE_HOST'] = config_parser.get(
                'config', 'host')
        else:
            app.config['MYSQL_DATABASE_USER'] = os.environ['DATABASE_USER']
            app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['DATABASE_PASSWORD']
            app.config['MYSQL_DATABASE_DB'] = os.environ['DATABASE_DB']
            app.config['MYSQL_DATABASE_HOST'] = os.environ['DATABASE_HOST']
        Connection.mysql.init_app(app)

    @staticmethod
    def get_config():
        config_parser = configparser.RawConfigParser()
        config_file_path = r'DB/config.txt'
        config_parser.read(config_file_path)
        return config_parser
