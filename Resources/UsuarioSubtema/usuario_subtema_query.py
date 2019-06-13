from Querys.query import Query
import Resources.UsuarioSubtema.querys_constants as qc
import Utils.messages_constants as mc
from pymysql import Error


class UsuarioSubtemaQuery(Query):

    def update_porcentage(self, usuario_subtema):
        count = None
        id_tema = None
        id_asignatura = None
        try:
            with self.get_cursor() as cursor:
                exist = self.insert_usuario_subtema(cursor, usuario_subtema)
                if exist:
                    count = self.get_count(
                        cursor, tipo="subtema", id=usuario_subtema[1])
                    id_tema = count["id_tema"]
                    total_subtema = count["numero"]
                    self.set_porcentaje()
                    cursor.connection.commit()
                    return {'mensaje': mc.PORCENTAJE_UPDATED}, 201
                else:
                    return {'mensaje': mc.OK}, 200
        except Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            cursor.connection.rollback()
            return {'error': mc.DB_ERROR}, 500
        finally:
            cursor.close()

    def insert_usuario_subtema(self, cursor, usuario_subtema):
        count = self.exists(
            cursor, tipo="subtema", id=usuario_subtema[1], id_usuario=usuario_subtema[0])
        if count["numero"] is 0:
            query = self.get_insert_query(
                qc.USUARIO_SUBTEMA_COLUMNS, qc.USUARIO_SUBTEMA_TABLE)
            cursor.execute(query, usuario_subtema)
            return True
        else:
            return False

    def exists(self, cursor, **kwargs):
        if kwargs["tipo"] is "subtema":
            cursor.execute(qc.USUARIO_SUBTEMA_EXIST, [
                           kwargs["id"], kwargs["id_usuario"]])
        elif kwargs["tipo"] is "tema":
            cursor.execute(qc.USUARIO_TEMA_EXIST, [
                           kwargs["id"], kwargs["id_usuario"]])
        else:
            cursor.execute(qc.USUARIO_ASIGNATURA_EXIST, [
                           kwargs["id"], kwargs["id_usuario"]])
        return cursor.fetchall()[0]

    def get_count(self, cursor, **kwargs):
        if "id_usuario" not in kwargs:
            if kwargs["tipo"] is "subtema":
                cursor.execute(qc.SUBTEMA_COUNT, [kwargs["id"]])
            else:
                cursor.execute(qc.TEMA_COUNT, [kwargs["id"]])
        else:
            if kwargs["tipo"] is "subtema":
                cursor.execute(qc.USUARIO_SUBTEMA_COUNT, [
                               kwargs["id"], kwargs["id_usuario"]])
            else:
                cursor.execute(qc.USUARIO_TEMA_COUNT, [
                               kwargs["id"], kwargs["id_usuario"]])
        return cursor.fetchall()[0]

    def set_porcentaje(self, cursor, **kwargs):
        count = self.exists(
            cursor, tipo="tema", id=kwargs["id_tema"], id_usuario=kwargs["id_usuario"])
        if count["numero"] is 0:
            porcentaje = (1 / kwargs["total"]) * 100
            query = self.get_insert_query(
                qc.USUARIO_TEMA_COLUMNS, qc.USUARIO_TEMA_TABLE)
            cursor.execute(
                query, [kwargs["id_usuario"], kwargs["id_tema"], int(porcentaje)])
            # insertar usuario_Asignatura
        else:
            count = self.get_count(
                cursor, tipo="subtema", id=kwargs["id_tema"], id_usuario=kwargs["id_usuario"])
            porcentaje = (count["numero"] / kwargs["total"]) * 100
            query = self.get_update_query(
                qc.PORCENTAJE_COLUMN, qc.USUARIO_TEMA_TABLE, qc.USUARIO_TEMA_WHERE_COLUMN)
            cursor.execute(
                query, [int(porcentaje), kwargs["id_usuario"], kwargs["id_tema"]])
            # evaluar si porcentaje es 100
