import datetime
from django.db import models
from organizations.models import Organizations

# Por defecto: null=False y blank=False

class ProjectEnum(models.TextChoices):
    PERSONAL = "P", "Personal"
    ORGANIZATIONAL = "O", "Organizacional"

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=32)
    description = models.TextField(null=True)
    organization_fk = models.ForeignKey(Organizations,
                                        on_delete=models.CASCADE,
                                        # Organization.objects.get(id=1).projects para obtener los proyectos de esta
                                        related_name="projects")
    # Nota: "tipe" fue escrito así para evitar la palabra reservada type()
    tipe = models.CharField(choices=ProjectEnum)
    creation_date = models.DateField(default=datetime.date.today)