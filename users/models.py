from django.db import models
from django.contrib.auth.models import AbstractBaseUser

import datetime

"""
    AbstractBaseUser ya tiene:
        - Campos: password y last_login
        - Hasheo de contraseña
        - Autentificación (usando authenticate())
"""
# Por defecto: null=False y blank=False
class Users(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    email = models.EmailField(unique=True, max_length=32)
    first_name = models.CharField(max_length=16, null=True, blank=True)
    last_name = models.CharField(max_length=16, null=True, blank=True)
    organization_fk = models.ForeignKey("organizations.Organizations", 
                                        on_delete=models.SET_NULL, 
                                        null=True,
                                        related_name="users")# related_name permite acceder desde la organización haciendo:
                                                            # Organizations.objects.get(id=1).users.all()

class InvitationsEnum(models.TextChoices):
    PENDING = "P", "Pendiente"
    ACCEPTED = "A", "Aceptada"
    REFUSED = "R", "Rechazada"

class Invitations(models.Model):
    id = models.AutoField(primary_key=True)
    organization_fk = models.ForeignKey("organizations.Organizations",
                                        on_delete=models.CASCADE)
    receiver_email = models.EmailField()
    receiver_fk = models.ForeignKey(Users,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    # Users.objects.get(id=x).received_invitations.all()
                                    related_name="received_invitations")
    sender_fk = models.ForeignKey(Users,
                                  on_delete=models.CASCADE, # Cascade por si se borró una cuenta que spammeaba
                                  # Users.objects.get(id=x).sended_invitations.all()
                                  related_name="sended_invitations") 
    state = models.CharField(max_length=1,
                             choices=InvitationsEnum,
                             default=InvitationsEnum.PENDING)
    send_date = models.DateField(default=datetime.date.today)