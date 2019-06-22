import Resources.Asignatura.querys_constants as qc
from Querys.query import Query


class AsignaturaQuery(Query):

    def get_asignaturas(self):
        return self.execute_select(qc.ASIGNATURA_COLUMNS, qc.ASIGNATURA_TABLE)
