import Resources.Usuario.querys_constants as qc
import Resources.Usuario.params_constants as pc
from Utils.crypto import Crypto
from Querys.query import Query
from pymysql import Error


class UsuarioQuery(Query):

    def insert_usuario(self, usuario):
        usuario[1] = Crypto.get_crypto(usuario[1])
        try:
            with self.get_cursor() as cursor:
                if self.check_user(usuario[0], usuario[4]):
                    query = self.get_insert_query(pc.PARAMS, qc.USER_TABLE)
                    cursor.execute(query, usuario)
                    id_usuario = cursor.lastrowid
                    cursor.execute(qc.USUARIO_ASIGNATURA_ALL, [id_usuario])
                    self.get_connection().commit()
                    return 201
                else:
                    return 202
        except Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            self.get_connection().rollback()
            return 500
        finally:
            cursor.close()

    def check_user(self, usuario, correo):
        check = self.execute_custom_query(qc.UNIQUE_USER, [usuario, correo])
        return len(check) is 0

    def add_coins(self, id_usuario, monedas):
        return self.execute_update(qc.COINS_COLUMN, qc.USER_TABLE, [
            monedas], qc.USERID_WHERE_COLUMN, [id_usuario])
