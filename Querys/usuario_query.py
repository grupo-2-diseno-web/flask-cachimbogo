import Utils.querys_constants as querys_constants
import Utils.params_constants as params_constants
from Utils.utils import get_crypt
from Querys.query import execute_insert, execute_select, execute_join, execute_insert_into


def insert_usuario(values):
    values[1] = get_crypt(values[1])
    insert = execute_insert(params_constants.USUARIO_PARAMS,
                            querys_constants.USER_TABLE, values)
    if insert:
        usuario = execute_select(querys_constants.USERID_COLUMN,
                                 querys_constants.USER_TABLE, querys_constants.USER_WHERE_COLUMN, (values[0]))
        insert = execute_insert_into(
            querys_constants.USUARIO_ASIGNATURA_ALL, (usuario[0]['id_usuario'],))
    return insert


def select_usuario(username):
    return execute_select(querys_constants.USER_ALL, querys_constants.USER_TABLE, querys_constants.USER_WHERE_COLUMN, (username,))
