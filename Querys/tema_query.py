import Utils.querys_constants as querys_constants
from Querys.query import execute_select


def select_tema(id_asignatura):
    return execute_select(querys_constants.TEMA_COLUMN, querys_constants.TEMA_TABLE, querys_constants.ASIGNATURAID_WHERE, (id_asignatura,))
