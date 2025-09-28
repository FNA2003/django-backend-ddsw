# APP's propuesta (Django):
* *`users`*
    - Registro y login
    - Maneja autenticación y endpoints relacionados al usuario
    - Manejo de Invitaciones (*__N.S.__*)
    - _Nota:_ Extiende el modelo `AbstractBaseUser`

* *`organizations`*
  - CRUD de organizaciones
  - Permisos y roles dentro de la organización
  - Expulsar/salir de la organización

* *`projects`*
  - CRUD de proyectos (personales u organizacionales ~ si tenemos permisos)

* *`tasks`*
  - CRUD de tareas (Con Antecesoras, fechas, etc.)
  - Asignaciones a usuarios o grupos
  - Completar, editar, borrar

* *`groups`*
  - CRUD de grupos dentro de una organización

* *`calander`*
  - Muestra las tareas del mes de un usuario (personales y, organizaciones si está asignado)
  - _NOTA:_ Se piensa usar esta app para disminuir la lógica de las otras aplicaciones.