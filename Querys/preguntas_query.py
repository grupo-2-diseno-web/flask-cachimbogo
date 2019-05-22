import Utils.constants as constants
from Querys.query import execute_select


def get_id_pregunta(id_subtema):
    return execute_select(constants.PREGUNTAID_COLUMN, constants.PREGUNTA_TABLE,
                          constants.PREGUNTA_SUBTEMA_WHERE, (id_subtema,))


def get_pregunta_by_id(id_pregunta):
    return execute_select(constants.PREGUNTA_COLUMN, constants.PREGUNTA_TABLE,
                          constants.PREGUNTAID_WHERE, (id_pregunta,))
