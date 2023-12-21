
from django.db import models
from apps.usuarios.models import Usuario


class InformacionContacto(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creado = models.DateTimeField(auto_now_add=True, null=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    mensaje = models.TextField()
    user_leido = models.ForeignKey(
        Usuario, on_delete=models.SET_NULL, null=True)
    fecha_leido = models.DateTimeField( null=True)

    def __str__(self):
        return self.nombre
