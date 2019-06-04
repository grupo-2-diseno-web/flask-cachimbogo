import Resources.Tema.querys_constants as qc
from Querys.query import Query


class TemaQuery(Query):

    def select_tema(self, id_asignatura):
        return self.execute_select(qc.TEMA_COLUMN, qc.TEMA_TABLE, qc.ASIGNATURAID_WHERE, [id_asignatura, ])
