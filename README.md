# APP's propuesta (Django):
* *`access`*
    - Registro y login
    - Maneja autenticación y endpoints relacionados al usuario
    - _Nota:_ Extiende el modelo `AbstractBaseUser`

* *`invitations`*
    - Maneja la búsqueda de invitaciones pendientes de un usuario loggeado
    - Buscará las asignadas a este y, las que estén asignadas a su email (cuenta que no estuvo registrada)
    - El usuario logeado (de una organización, con permisos de invitar) podrá invitar a una lista de usuarios por mail (estén registrados o no).
    - Aceptar o rechazar invitaciones recibidas.
    - _TODO:_ Eliminar campo de sender_fk del modelo 

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

* *`date`*
  - Muestra las tareas del mes de un usuario (personales y, organizaciones si está asignado)
  - _NOTA:_ Se piensa usar esta app para disminuir la lógica de las otras aplicaciones.
