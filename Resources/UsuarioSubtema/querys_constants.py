# COLUMNS
USUARIO_SUBTEMA_COLUMNS = ["id_usuario", "id_subtema", "completado"]
USUARIO_TEMA_COLUMNS = ["id_usuario", "id_tema", "porcentaje"]
PORCENTAJE_COLUMN = ["porcentaje"]

# TABLES
USUARIO_SUBTEMA_TABLE = "usuario_subtema"
USUARIO_TEMA_TABLE = "usuario_tema"

# WHERE COLUMN
PREGUNTAID_WHERE_COLUMN = ["id_pregunta"]
USERID_WHERE_COLUMN = ["id_usuario"]
USUARIO_TEMA_WHERE_COLUMN = ["id_usuario", "id_tema"]

# COUNTS
SUBTEMA_COUNT = "SELECT id_tema AS id, COUNT(*) AS numero FROM subtema WHERE id_tema = (SELECT id_tema FROM subtema WHERE id_subtema = %s);"
TEMA_COUNT = "SELECT id_asignatura AS id, COUNT(*) AS numero FROM tema WHERE id_asignatura = (SELECT id_asignatura FROM tema WHERE id_tema = %s);"
USUARIO_SUBTEMA_COUNT = "SELECT count(*) AS numero FROM usuario_subtema WHERE id_subtema in (SELECT id_subtema FROM subtema WHERE id_tema = %s) AND id_usuario = %s AND completado = 1;"
USUARIO_TEMA_COUNT = "SELECT count(*) AS numero FROM usuario_tema WHERE id_tema in (SELECT id_tema from tema where id_asignatura = %s) and id_usuario = %s and porcentaje = 100;"

# EXIST
USUARIO_SUBTEMA_EXIST = "SELECT count(*) AS numero FROM usuario_subtema WHERE id_subtema= %s AND id_usuario = %s;"
USUARIO_TEMA_EXIST = "SELECT count(*) AS numero FROM usuario_tema WHERE id_tema = %s AND id_usuario = %s;"
USUARIO_ASIGNATURA_EXIST = "SELECT count(*) AS numero FROM usuario_asignatura WHERE id_asignatura= %s AND id_usuario = %s;"
