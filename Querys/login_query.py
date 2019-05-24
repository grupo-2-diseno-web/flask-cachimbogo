from Utils.utils import get_crypt
from Querys.query import execute_select
import Utils.constants as constants


def user_exists(username):
    data = execute_select(constants.USER_COLUMN,
                          constants.USER_TABLE, constants.USER_WHERE_COLUMN, (username,))
    return len(data) is not 0


def is_password(username, password):
    data = execute_select(constants.PASSWORD_COLUMN,
                          constants.USER_TABLE, constants.USER_WHERE_COLUMN, (username,))
    if len(data) is not 0:
        password_hash = get_crypt(password)
        password_selected = data[0]["password"]
        return password_hash == password_selected
    else:
        return False
