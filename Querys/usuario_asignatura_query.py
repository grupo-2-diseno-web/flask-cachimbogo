import Utils.querys_constants as querys_constants
from Querys.query import execute_join


def select_usuario_asignatura(id_usuario):
    return execute_join(querys_constants.USUARIO_ASIGNATURA, (id_usuario,))
