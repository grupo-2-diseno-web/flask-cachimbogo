from Querys.query import execute_select
import Resources.Respuesta.querys_constants as qc


def check_answer(id_pregunta, correcta_num):
    correct_num_selected = execute_select(qc.RESPUESTA_COLUMN, 
                                          qc.PREGUNTA_TABLE, 
                                          qc.PREGUNTAID_WHERE, (id_pregunta))
    correcta = correcta_num == correct_num_selected[0]["correcta_num"]
    informacion = correct_num_selected[0]["informacion"]
    return {'correcta': correcta, 'informacion': informacion}