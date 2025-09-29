from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Por defecto, todos los campos son: null=False y blank=False


# Manager personalizado para crear instancias de Users en django.
# Se usa para hashing y autentificación de usuarios.
class UsersManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        if not password:
            raise ValueError("La contraseña es obligatorio")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields) # Actualizamos el modelo (si no falla otro campo)
        user.set_password(password)                                       # Acá se hashea la contraseña
        user.save(using=self._db)                                         # Se intenta salvar en la bdd definida por django
        return user                                                       # Y, se retorna

class Users(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    email = models.EmailField(unique=True, max_length=32)
    first_name = models.CharField(max_length=16, null=True, blank=True)
    last_name = models.CharField(max_length=16, null=True, blank=True)
    organization_fk = models.ForeignKey("organizations.Organizations", 
                                        on_delete=models.SET_NULL, 
                                        null=True,
                                        blank=True,
                                        related_name="users")# related_name permite acceder desde la organización haciendo:
                                                             # Organizations.objects.get(id=1).users.all()
    
    objects = UsersManager()         # Define cómo se crean y gestionan los usuarios
    USERNAME_FIELD = 'email'         # El email será el identificador ÚNICO para login
    REQUIRED_FIELDS = ['username']   # Además del email, se requiere el username al crear usuarios