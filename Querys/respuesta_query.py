from Querys.query import execute_select
import Utils.querys_constants as querys_constants


def check_answer(id_pregunta, correcta_num):
    correct_num_selected = execute_select(querys_constants.RESPUESTA_COLUMN, 
                                          querys_constants.PREGUNTA_TABLE, 
                                          querys_constants.PREGUNTAID_WHERE, (id_pregunta))
    correcta = correcta_num == correct_num_selected[0]["correcta_num"]
    informacion = correct_num_selected[0]["informacion"]
    return {'correcta': correcta, 'informacion': informacion}