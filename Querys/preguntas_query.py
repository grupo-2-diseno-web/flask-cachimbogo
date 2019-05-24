import Utils.constants as constants
from Querys.query import execute_select
from random import choice


def get_id_pregunta(id_subtema):
    return execute_select(constants.PREGUNTAID_COLUMN, constants.PREGUNTA_TABLE,
                          constants.PREGUNTA_SUBTEMA_WHERE, (id_subtema,))


def get_pregunta_by_id(id_pregunta):
    return execute_select(constants.PREGUNTA_COLUMN, constants.PREGUNTA_TABLE,
                          constants.PREGUNTAID_WHERE, (id_pregunta,))


def get_random_questions(id_subtema, completado):
    id_preguntas = get_id_pregunta(id_subtema)
    random_questions = []
    id_selected = []
    cantidad = 7
    if completado is 0:
        cantidad = 10
    i = 1
    while i <= cantidad:
        random_id = choice(id_preguntas)["id_pregunta"]
        if random_id not in id_selected:
            id_selected.append(random_id)
            random_questions.append(get_pregunta_by_id(random_id)[0])
            i += 1
    return random_questions
