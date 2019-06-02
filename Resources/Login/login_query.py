from Utils.utils import get_crypto, check_crypto
from Querys.query import execute_select
import Resources.Login.querys_constants as qc


def user_exists(username):
    data = execute_select(qc.USER_COLUMN,
                          qc.USER_TABLE, qc.USER_WHERE_COLUMN, (username,))
    return len(data) is not 0


def is_password(username, password):
    data = execute_select(qc.PASSWORD_COLUMN,
                          qc.USER_TABLE, qc.USER_WHERE_COLUMN, (username,))
    if len(data) is not 0:
        return check_crypto(data[0]["password"], password)
    else:
        return False

def select_usuario(username):
    return execute_select(qc.USER_ALL, qc.USER_TABLE, qc.USER_WHERE_COLUMN, (username,))
