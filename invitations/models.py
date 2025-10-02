from django.db import models

import datetime

class InvitationsEnum(models.TextChoices):
    PENDING = "P", "Pendiente"
    ACCEPTED = "A", "Aceptada"
    REFUSED = "R", "Rechazada"

class Invitations(models.Model):
    id = models.AutoField(primary_key=True)
    organization_fk = models.ForeignKey("organizations.Organizations",
                                        on_delete=models.CASCADE)
    receiver_email = models.EmailField()
    sender_fk = models.ForeignKey("access.Users",
                                  on_delete=models.CASCADE, # Cascade por si se borró una cuenta que spammeaba
                                  # Users.objects.get(id=x).sended_invitations.all()
                                  related_name="sended_invitations") 
    state = models.CharField(max_length=1,
                             choices=InvitationsEnum,
                             default=InvitationsEnum.PENDING)
    send_date = models.DateField(default=datetime.date.today)