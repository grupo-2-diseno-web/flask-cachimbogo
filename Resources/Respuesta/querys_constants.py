# COLUMNS
RESPUESTA_COLUMN = ["correcta_num", "informacion"]
COINS_COLUMN = ["monedas"]
RESPUESTA_COLUMNS = ["id_usuario", "id_pregunta", "acertada"]

# TABLES
PREGUNTA_TABLE = "pregunta"
USER_TABLE = "usuario"
RESPUESTA_TABLE = "respuesta"

# WHERE COLUMN
PREGUNTAID_WHERE_COLUMN = ["id_pregunta"]
USERID_WHERE_COLUMN = ["id_usuario"]

# COUNT
RESPUESTA_COUNT = "SELECT count(*) AS numero FROM respuesta WHERE id_usuario = %s AND id_pregunta = %s"
