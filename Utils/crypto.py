from flask_bcrypt import Bcrypt


class Crypto(object):

    bcrypt = None

    def __init__(self):
        pass
    
    def init_crypto(self, app):
        app.config['BCRYPT_HANDLE_LONG_PASSWORDS'] = True
        Crypto.bcrypt = Bcrypt(app)