from django.urls import path
from . import views

app_name = 'acercade'

urlpatterns = [
    path('', views.formulario_contacto, name='acercade'),
    path('exito/', views.exito, name='exito'),
    path('mensajes/', views.mensajes, name='mensajes'),
]

