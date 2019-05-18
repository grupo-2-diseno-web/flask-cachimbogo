from DB.connection import Connection
from Utils.utils import get_select_query
import Utils.constants as constants


def get_id_pregunta(id_subtema):
    conn = Connection.mysql.connect()
    cursor = conn.cursor()
    query = get_select_query(constants.PREGUNTAID_COLUMN, constants.PREGUNTA_TABLE,
        constants.PREGUNTA_SUBTEMA_WHERE)
    cursor.execute(query, (id_subtema,))
    data = cursor.fetchall()
    cursor.close()
    return data


def get_pregunta_by_id(id_pregunta):
    conn = Connection.mysql.connect()
    cursor = conn.cursor()
    query = get_select_query(constants.PREGUNTA_COLUMN, constants.PREGUNTA_TABLE,
        constants.PREGUNTAID_WHERE)
    cursor.execute(query, (id_pregunta,))
    data = cursor.fetchall()
    cursor.close()
    return data
