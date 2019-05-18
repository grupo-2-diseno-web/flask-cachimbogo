from DB.connection import Connection
from Utils.utils import get_crypt, get_select_query
import Utils.constants as constants


def user_exists(username):
    conn = Connection.mysql.connect()
    cursor = conn.cursor()
    query = get_select_query(constants.USER_COLUMN, constants.USER_TABLE,constants.USER_WHERE_COLUMN)
    cursor.execute(query, (username,))
    data = cursor.fetchall()
    cursor.close()
    return len(data) is not 0


def is_password(username, password):
    conn = Connection.mysql.connect()
    cursor = conn.cursor()
    query = get_select_query(constants.PASSWORD_COLUMN, constants.USER_TABLE, constants.USER_WHERE_COLUMN)
    cursor.execute(query, (username,))
    data = cursor.fetchall()
    cursor.close()
    password_hash = get_crypt(password)
    password_selected = data[0][0]
    return password_hash == password_selected
