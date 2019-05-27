# LOGIN RESOURCE
LOGIN_PARAMS = ["username", "password"]
LOGIN_PARAMS_TYPE = ["string", "string"]
LOGIN_PARAMS_HELP = ['Username to authenticate', 'Password to create user']

# PREGUNTA RESOURCE
PREGUNTA_PARAMS = ["enunciado", "clave1",
                   "clave2", "clave3", "clave4",
                   "clave5", "estado", "id_subtema",
                   "id_tipopregunta", "id_dificultad", "informacion"]
PREGUNTA_PARAMS_TYPE = ["string", "string",
                        "string", "string", "string",
                        "string", "int", "int", "int",
                        "int", "string"]
PREGUNTA_PARAMS_HELP = ["Enunciado de la pregunta",
                        "Primera clave de la pregunta", "Segunda clave de la pregunta", "Tercera clave de la pregunta",
                        "Cuarta clave de la pregunta", "Quinta clave de la pregunta", "Estado de la pregunta",
                        "ID del subtema", "ID tipo pregunta", "ID de la dificultad", "Informacion de la respuesta"]

# USUARIO RESOURCE
USUARIO_PARAMS = ["usuario", "password",
                  "nombres", "apellidos", "correo", "monedas"]
USUARIO_PARAMS_TYPE = ["string", "string", "string", "string", "string", "int"]
USUARIO_PARAMS_HELP = ["Nombre del usuario", "Contraseña del usuario", "Nombres del usuario", "Apellidos del usuario",
                       "Correo del usuario", "Monedas del usuario"]
