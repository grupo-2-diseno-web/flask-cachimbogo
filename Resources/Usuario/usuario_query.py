import Resources.Usuario.querys_params as qc
import Resources.Usuario.params_constants as pc
from Utils.crypto import Crypto
from Querys.query import Query
from pymysql import Error


class UsuarioQuery(Query):

    def insert_usuario(self, usuario):
        usuario[1] = Crypto.get_crypto(usuario[1])
        try:
            with self.get_cursor() as cursor:
                query = self.get_insert_query(pc.PARAMS, qc.USER_TABLE)
                cursor.execute(query, usuario)
                id_usuario = cursor.lastrowid
                cursor.execute(qc.USUARIO_ASIGNATURA_ALL, [id_usuario])
                cursor.connection.commit()
                return True
        except Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            cursor.connection.rollback()
            return False
        finally:
            cursor.close()


def check_user(username, email):
    # select verificando usuario y correo
    pass
