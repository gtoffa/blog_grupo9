
from django.db import models
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from apps.usuarios.models import Usuario
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, CHANGE
from model_utils import FieldTracker
from apps.noticias.middleware import get_current_user

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    # = VARCHAR | max_length longitud max
    titulo = models.CharField(max_length=255)
    # Uso de ckeditor para usar el edito html
    contenido = RichTextField()
    resumen = models.CharField(max_length=200, null=True)
    # imagen requiere la libreria pillow
    imagenes = models.ImageField(upload_to='noticias')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria_noticia = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)

    cant_vistas = models.IntegerField(default=0)
    # Para poder default=Usuario.objects.get(is_superuser=True).pk tiene que existir el super usuario
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    # Usamos FieldTracker para realizar un seguimiento de los cambios en los campos

    tracker = FieldTracker()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    noticia = models.ForeignKey(
        Noticia, on_delete=models.CASCADE, related_name='comentarios',)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.contenido


# Definir una función para manejar la lógica de detección de cambios y guardar en LogEntry
@receiver(post_save, sender=Noticia)
def detectar_y_guardar_cambios(sender, instance, created, **kwargs):
    # Verificar si se está creando un nuevo objeto (en lugar de actualizar)
    guardar = False
    if created:
        change_message= "Se crea Articulo"
        guardar = True

    else:
        changes = []
        # Crear una nueva entrada de historial solo si hay cambios
        change_message = "Modificación de: "
        

        if instance.tracker.has_changed('titulo'):
            changes.append("titulo")
            guardar = True
        if instance.tracker.has_changed('contenido'):
            changes.append("contenido")
            guardar = True

        if instance.tracker.has_changed('resumen'):
            changes.append("resumen")
            guardar = True

        if instance.tracker.has_changed('imagenes'):
            changes.append("imagenes")
            guardar = True

        if instance.tracker.has_changed('categoria_noticia_id'):
            changes.append("categoria noticia")
            guardar = True

        # Concatenar los cambios acumulados
        change_message += ", ".join(changes)

        
    if guardar:
        user = get_current_user()
        content_type = ContentType.objects.get_for_model(instance)
        LogEntry.objects.create(
            content_type=content_type,
            object_id=instance.pk,
            object_repr=str(instance),
            action_flag=CHANGE,
            user_id=user.pk,
            change_message=change_message,
        )


# Registrar la función para escuchar la señal post_save
post_save.connect(detectar_y_guardar_cambios, sender=Noticia)
