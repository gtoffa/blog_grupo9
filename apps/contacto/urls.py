from django.urls import path
from . import views

app_name = 'contacto'

urlpatterns = [
    path('', views.formulario_contacto, name='contacto'),
    path('exito/', views.exito, name='exito'),
]

