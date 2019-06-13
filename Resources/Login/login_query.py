from Utils.crypto import Crypto
from Querys.query import Query
import Resources.Login.querys_constants as qc


class LoginQuery(Query):

    def user_exists(self, username):
        data = self.execute_select(qc.USER_COLUMN,
                                   qc.USER_TABLE, qc.USER_WHERE_COLUMN, [username, ])
        return len(data) is not 0

    def is_password(self, username, password):
        data = self.execute_select(qc.PASSWORD_COLUMN,
                                   qc.USER_TABLE, qc.USER_WHERE_COLUMN, [username, ])
        print(data)
        if len(data) is not 0:
            return Crypto.check_crypto(data[0]["password"], password)
        else:
            return False

    def select_usuario(self, username):
        return self.execute_select(qc.USER_ALL, qc.USER_TABLE, qc.USER_WHERE_COLUMN, [username, ])
