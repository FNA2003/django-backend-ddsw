from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.TextField(null=False) # dbdiagram -> varchar <=> text
    email = models.EmailField(null=False, unique=True)
    password = models.TextField(null=False)


    # Métodos para hashear y comprobar la contraseña
    def set_password(self, contrasena_plana):
        self.password = make_password(contrasena_plana)
    def check_password(self, contrasena_plana):
        return check_password(contrasena_plana, self.password)
    
    def __str__(self):
        return "User id: " + str(self.user_id) + " Usename: " + self.name + " User email: " + self.email