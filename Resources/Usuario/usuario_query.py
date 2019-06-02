import Resources.Usuario.querys_params as qc
import Resources.Usuario.params_constants as pc
from Utils.utils import get_crypto
from Querys.query import execute_insert, execute_select, execute_join, execute_insert_into


def insert_usuario(values):
    values[1] = get_crypto(values[1])
    insert = execute_insert(pc.PARAMS,
                            qc.USER_TABLE, values)
    if insert:
        usuario = execute_select(qc.USERID_COLUMN,
                                 qc.USER_TABLE, qc.USER_WHERE_COLUMN, (values[0]))
        insert = execute_insert_into(
            qc.USUARIO_ASIGNATURA_ALL, (usuario[0]['id_usuario'],))
    return insert


def check_user(username, email):
    exists = execute_select()
