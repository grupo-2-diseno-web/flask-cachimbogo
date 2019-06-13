from Querys.query import Query
import Resources.Respuesta.querys_constants as qc
import Utils.messages_constants as mc
from pymysql import Error


class RespuestaQuery(Query):

    def check_answer(self, respuesta):
        try:
            with self.get_cursor() as cursor:
                check = self.__is_answer(respuesta[1], respuesta[2])
                if check[0]:
                    # Agrega 4 monedas
                    query = self.get_update_query(
                        qc.COINS_COLUMN, qc.USER_TABLE, qc.USERID_WHERE_COLUMN)
                    cursor.execute(query, [4, respuesta[0]])
                    # insertar respuesta
                query = self.get_insert_query(
                    qc.RESPUESTA_COLUMNS, qc.RESPUESTA_TABLE)
                cursor.execute(query, respuesta[0:2] + check[0:1])
                cursor.connection.commit()
                return {'correcta': check[0], 'informacion': check[1]}, 200
        except Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            cursor.connection.rollback()
            return {'error': mc.DB_ERROR}, 500
        finally:
            cursor.close()

    def __is_answer(self, id_pregunta, correcta_num):
        correct_num_selected = self.execute_select(qc.RESPUESTA_COLUMN,
                                                   qc.PREGUNTA_TABLE,
                                                   qc.PREGUNTAID_WHERE_COLUMN, [id_pregunta])
        correcta = correcta_num == correct_num_selected[0]["correcta_num"]
        informacion = correct_num_selected[0]["informacion"]
        return [correcta, informacion]
