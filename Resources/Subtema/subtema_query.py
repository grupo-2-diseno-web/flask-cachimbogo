import Utils.querys_constants as querys_constants
from Querys.query import execute_select


def select_subtema(id_tema):
    return execute_select(querys_constants.SUBTEMA_COLUMN, querys_constants.SUBTEMA_TABLE, querys_constants.TEMAID_WHERE, (id_tema,))
