
from django.db import models

class InformacionContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
