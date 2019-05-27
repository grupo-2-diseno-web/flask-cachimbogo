import Utils.querys_constants as querys_constants
import Utils.params_constants as params_constants
from Querys.query import execute_select, execute_join, execute_insert
from random import choice


def get_id_pregunta(id_subtema):
    return execute_select(querys_constants.PREGUNTAID_COLUMN, querys_constants.PREGUNTA_TABLE,
                          querys_constants.PREGUNTA_SUBTEMA_WHERE, (id_subtema,))


def get_pregunta_by_id(id_pregunta):
    return execute_select(querys_constants.PREGUNTA_COLUMN, querys_constants.PREGUNTA_TABLE,
                          querys_constants.PREGUNTAID_WHERE, (id_pregunta,))


def get_random_questions(id_subtema, completado):
    id_preguntas = get_id_pregunta(id_subtema)
    random_questions = []
    id_selected = []
    cantidad = 7
    if completado is 0:
        cantidad = 10
    i = 1
    while i <= cantidad:
        random_id = choice(id_preguntas)
        id_preguntas.remove(random_id)
        random_questions.append(
            get_pregunta_by_id(random_id["id_pregunta"])[0])
        i += 1
    return random_questions


def get_pregunta_by_subtema(id_subtema):
    return execute_select(querys_constants.PREGUNTA_COLUMN, querys_constants.PREGUNTA_TABLE,
                          querys_constants.PREGUNTA_SUBTEMA_WHERE, (id_subtema,))


def get_pregunta_populate(id_pregunta):
    return execute_join(querys_constants.PREGUNTA_POPULATE, (id_pregunta,))


def insert_pregunta(values):
    return execute_insert(params_constants.PREGUNTA_PARAMS, querys_constants.PREGUNTA_TABLE, values)
