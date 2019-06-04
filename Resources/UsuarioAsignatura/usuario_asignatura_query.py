import Resources.UsuarioAsignatura.querys_constants as qc
from Querys.query import Query


class UsuarioAsignaturaQuery(Query):

    def select_usuario_asignatura(self, id_usuario):
        return self.execute_join(qc.USUARIO_ASIGNATURA, (id_usuario,))
