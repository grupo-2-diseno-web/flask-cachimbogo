import Resources.UsuarioAsignatura.querys_constants as qc
from Querys.query import Query


class UsuarioAsignaturaQuery(Query):

    def select_usuario_asignatura(self, id_usuario):
        return self.execute_custom_query(qc.USUARIO_ASIGNATURA, [id_usuario, ])
