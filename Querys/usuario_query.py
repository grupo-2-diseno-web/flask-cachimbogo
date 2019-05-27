import Utils.querys_constants as querys_constants
import Utils.params_constants as params_constants
from Utils.utils import get_crypt
from Querys.query import execute_insert


def insert_usuario(values):
    values[1] = get_crypt(values[1])
    return execute_insert(params_constants.USUARIO_PARAMS, querys_constants.USER_TABLE, values)
