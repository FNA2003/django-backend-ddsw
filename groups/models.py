from django.db import models

# Por defecto: null=False y blank=False

class Groups(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    description = models.TextField(blank=True, null=True)
    organization_fk = models.ForeignKey("organizations.Organizations",
                                        on_delete=models.CASCADE,
                                        # related_name => Organizations.objects.get(id=x).groups.all()
                                        related_name="groups")
    members_fk = models.ManyToManyField("users.Users",
                                        # related_name => Users.objects.get(id=x).in_groups.all()
                                        related_name="in_groups")