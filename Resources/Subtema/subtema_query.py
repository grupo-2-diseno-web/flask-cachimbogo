import Resources.Subtema.querys_constants as qc
from Querys.query import Query


class SubtemaQuery(Query):

    def get_subtemas(self, id_tema):
        return self.execute_select(qc.SUBTEMA_COLUMN, qc.SUBTEMA_TABLE, qc.TEMAID_WHERE, [id_tema, ])
