# COLUMNS
USERID_COLUMN = ["id_usuario"]
COINS_COLUMN = ["monedas"]

# TABLES
USER_TABLE = "usuario"

# WHERE COLUMN
USER_WHERE_COLUMN = ["usuario"]
USERID_WHERE_COLUMN = ["id_usuario"]
CHECK_WHERE_COLUMN = ["usuario", "correo"]


# INSERT INTO
USUARIO_ASIGNATURA_ALL = "INSERT INTO usuario_asignatura SELECT %s, id_asignatura, 0 FROM asignatura WHERE id_asignatura NOT IN (19,8)"
