# COLUMNS
USER_COLUMN = ["usuario"]
USERID_COLUMN = ["id_usuario"]
USER_ALL = ["id_usuario", "usuario", "nombres",
            "apellidos", "correo", "monedas"]
PASSWORD_COLUMN = ["password"]
PREGUNTAID_COLUMN = ["id_pregunta"]
PREGUNTA_COLUMN = ["id_pregunta", "enunciado", "clave1", "clave2", "clave3", "clave4",
                   "clave5", "estado", "informacion", "id_dificultad"]
RESPUESTA_COLUMN = ["correcta_num", "informacion"]

# TABLES
PREGUNTA_TABLE = "pregunta"
USER_TABLE = "usuario"

# WHERE COLUMN
USER_WHERE_COLUMN = ["usuario"]
PREGUNTA_SUBTEMA_WHERE = ["id_subtema"]
PREGUNTAID_WHERE = ["id_pregunta"]

# JOIN SQL
PREGUNTA_POPULATE = "SELECT p.id_pregunta, p.enunciado, p.clave1, p.clave2, p.clave3, p.clave4, p.clave5, p.estado, p.informacion, s.id_subtema, s.nombre, t.id_tema, t.nombre, a.id_asignatura, a.nombre FROM pregunta p INNER JOIN subtema s ON p.id_subtema = s.id_subtema INNER JOIN tema t ON s.id_tema = t.id_tema INNER JOIN asignatura a ON t.id_asignatura = a.id_asignatura WHERE p.id_pregunta = %s;"
USUARIO_ASIGNATURA = "SELECT a.id_asignatura, a2.nombre, a.porcentaje FROM usuario_asignatura AS a INNER JOIN asignatura a2 ON a.id_asignatura = a2.id_asignatura WHERE a.id_usuario = %s;"

# INSERT INTO
USUARIO_ASIGNATURA_ALL = "INSERT INTO usuario_asignatura SELECT %s, id_asignatura, 0 FROM asignatura WHERE id_asignatura NOT INT (19,8)"