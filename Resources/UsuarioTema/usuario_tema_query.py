import Resources.UsuarioTema.querys_constants as qc
from Querys.query import Query


class UsuarioTemaQuery(Query):

    def select_usuario_tema(self, id_usuario, id_asignatura):
        return self.execute_custom_query(qc.USUARIO_TEMA, [id_usuario, id_asignatura])
