import Resources.Pregunta.querys_constants as qc
import Resources.Pregunta.params_constants as pc
from Querys.query import Query
from random import choice


class PreguntaQuery(Query):

    def get_id_pregunta(self, id_subtema):
        return self.execute_select(qc.PREGUNTAID_COLUMN, qc.PREGUNTA_TABLE,
                                   qc.PREGUNTA_SUBTEMA_WHERE, (id_subtema,))

    def get_pregunta_by_id(self, id_pregunta):
        return self.execute_select(qc.PREGUNTA_COLUMN, qc.PREGUNTA_TABLE,
                                   qc.PREGUNTAID_WHERE, (id_pregunta,))

    def get_random_questions(self, id_subtema, completado):
        id_preguntas = self.get_id_pregunta(id_subtema)
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
                self.get_pregunta_by_id(random_id["id_pregunta"])[0])
            i += 1
        return random_questions

    def get_pregunta_by_subtema(self, id_subtema):
        return self.execute_select(qc.PREGUNTA_COLUMN, qc.PREGUNTA_TABLE,
                                   qc.PREGUNTA_SUBTEMA_WHERE, (id_subtema,))

    def get_pregunta_populate(self, id_pregunta):
        return self.execute_join(qc.PREGUNTA_POPULATE, (id_pregunta,))

    def insert_pregunta(self, values):
        return self.execute_insert(pc.PARAMS, qc.PREGUNTA_TABLE, values)
