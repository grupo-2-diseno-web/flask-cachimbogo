from DB.connection import Connection
from Utils.utils import get_crypt


def user_exists(username):
    conn = Connection.mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT usuario FROM usuario WHERE usuario =%s;", (username,))
    data = cursor.fetchall()
    cursor.close()
    return len(data) is not 0


def is_password(username, password):
    conn = Connection.mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password FROM usuario WHERE usuario =%s;", (username,))
    data = cursor.fetchall()
    cursor.close()
    password_hash = get_crypt(password)
    password_selected = data[0][0]
    return password_hash == password_selected
