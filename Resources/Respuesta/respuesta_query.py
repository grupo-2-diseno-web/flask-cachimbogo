from Querys.query import Query
import Resources.Respuesta.querys_constants as qc


class RespuestaQuery(Query):

    def check_answer(self, id_pregunta, correcta_num):
        correct_num_selected = self.execute_select(qc.RESPUESTA_COLUMN, 
                                            qc.PREGUNTA_TABLE, 
                                            qc.PREGUNTAID_WHERE, (id_pregunta))
        correcta = correcta_num == correct_num_selected[0]["correcta_num"]
        informacion = correct_num_selected[0]["informacion"]
        return {'correcta': correcta, 'informacion': informacion}