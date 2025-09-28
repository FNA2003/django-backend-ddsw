from django.db import models
import datetime

# Por defecto: null=False y blank=False

class ProjectEnum(models.TextChoices):
    PERSONAL = "P", "Personal"
    ORGANIZATIONAL = "O", "Organizacional"

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    description = models.TextField(null=True)
    organization_fk = models.ForeignKey("organizations.Organizations",
                                        on_delete=models.CASCADE,
                                        null=True,
                                        # Organization.objects.get(id=1).projects para obtener los proyectos de esta
                                        related_name="projects")
    # Nota: "tipe" fue escrito así para evitar la palabra reservada type()
    tipe = models.CharField(max_length=1, choices=ProjectEnum)
    creation_date = models.DateField(default=datetime.date.today)