from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.UltimasNoticias, name='home')
]