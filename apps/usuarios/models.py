from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    imagenes = models.ImageField(upload_to='user', default='user/avatar.svg')  # Establecer la imagen por defecto



    def __str__(self):
       return f"{self.first_name} {self.last_name}" 