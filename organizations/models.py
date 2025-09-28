import datetime
from django.db import models
from users.models import Users

# Por defecto: null=False y blank=False
class Organizations(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=16)
    description = models.TextField(null=True, blank=True)
    creation_date = models.DateField(default=datetime.date.today)


# Enum de los roles dentro de la organización
class EnumPermisos(models.TextChoices):
    CREATOR = "C", "Creador"
    ADMIN = "A", "Administrador"
    MEMBER = "M", "Miembro"

class PermissionsOrganization(models.Model):
    id = models.AutoField(primary_key=True)
    organization_fk = models.ForeignKey(Organizations, 
                                        on_delete=models.CASCADE)
    # Nota: Usamos OneToOneField y no ForeingKey por que la lógica
    # de nuestro negocio solo nos deja tener un usuario por organización
    user_fk = models.OneToOneField(Users,
                                   on_delete=models.CASCADE,
    # El related_name nos permite: Users.objects.get(id=1).org_perm_user <= De acá sacaríamos los permisos del usuario
                                   related_name="org_perm_user")
    role = models.CharField(
        max_length=1,
        choices=EnumPermisos,
        default=EnumPermisos.MEMBER
    )
    # Permisos, sobre estos se consultará luego
    can_complete_tasks     = models.BooleanField(default=True)
    can_edit_tasks         = models.BooleanField(default=False)
    can_create_tasks       = models.BooleanField(default=False)
    can_create_projects    = models.BooleanField(default=False)
    can_edit_projects      = models.BooleanField(default=False)
    can_assign_permissions = models.BooleanField(default=False)
    can_close_organization = models.BooleanField(default=False)