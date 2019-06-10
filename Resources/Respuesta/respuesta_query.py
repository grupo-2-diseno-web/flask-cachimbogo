from Querys.query import Query
import Resources.Respuesta.querys_constants as qc
from pymysql import Error


class RespuestaQuery(Query):

    def check_answer(self, id_usuario, id_pregunta, correcta_num):
        try:
            with self.get_cursor() as cursor:
                check = self.is_answer(id_pregunta, correcta_num)
                if check[0]:
                    query = self.get_update_query(
                        qc.COINS_COLUMN, qc.USER_TABLE, qc.USERID_WHERE)
                    cursor.execute(query, [4, id_usuario])
                    # insertar pregunta
                    cursor.connection.commit()
                    return 201
                return {'correcta': check[0], 'informacion': check[1]}
        except Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            cursor.connection.rollback()
            return {'error': mc.DB_ERROR}, 500
        finally:
            cursor.close()

    def is_answer(self, id_pregunta, correcta_num):
        correct_num_selected = self.execute_select(qc.RESPUESTA_COLUMN,
                                                   qc.PREGUNTA_TABLE,
                                                   qc.PREGUNTAID_WHERE_COLUMN, [id_pregunta])
        correcta = correcta_num == correct_num_selected[0]["correcta_num"]
        informacion = correct_num_selected[0]["informacion"]
        return [correcta, informacion]
