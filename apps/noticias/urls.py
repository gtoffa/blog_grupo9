from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.ListarNoticias, name='listar'),
    path('detalle/<int:pk>', views.DetalleNoticia, name='detalle'), 
    #path('ajax/', views.EjemploAjax, name='ejemploajax'),
    #path('panel_noticias', views.PanelNoticias, name='panel_noticias'),
]