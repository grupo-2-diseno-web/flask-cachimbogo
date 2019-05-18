from DB.connection import Connection


def get_id_pregunta(id_subtema):
    conn = Connection.mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id_pregunta FROM pregunta where id_subtema = %s;", (id_subtema,))
    data = cursor.fetchall()
    cursor.close()
    return data


def get_pregunta_by_id(id_pregunta):
    conn = Connection.mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id_pregunta,enunciado,clave1,clave2,clave3,clave4,clave5,estado,informacion,id_dificultad "
        + "FROM cachimbogo.pregunta "
        + "where id_pregunta = %s;", (id_pregunta,))
    data = cursor.fetchall()
    cursor.close()
    return data
