USUARIO_ASIGNATURA = "SELECT a.id_asignatura, a2.nombre, a.porcentaje, a2.imagen FROM usuario_asignatura AS a INNER JOIN asignatura a2 ON a.id_asignatura = a2.id_asignatura WHERE a.id_usuario = %s;"
