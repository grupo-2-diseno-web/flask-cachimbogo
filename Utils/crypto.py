from flask_bcrypt import Bcrypt


class Crypto(object):

    bcrypt = None

    def __init__(self, app):
        app.config['BCRYPT_HANDLE_LONG_PASSWORDS'] = True
        Crypto.bcrypt = Bcrypt(app)

    
    @classmethod
    def get_crypto(cls, word):
        hash_bcrypt = cls.bcrypt.generate_password_hash(word)
        return hash_bcrypt
    

    @classmethod
    def check_crypto(cls, hash_bcrypt, word):
        return cls.bcrypt.check_password_hash(hash_bcrypt, word)