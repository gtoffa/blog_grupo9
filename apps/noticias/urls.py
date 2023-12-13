from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.ListarNoticias, name='listar'),
    path('detalle/<int:pk>', views.DetalleNoticia, name='detalle'), 
    path('detalle/ajax/cargar_comentarios/<int:noticia_id>/', views.cargar_comentarios, name='cargar_comentarios'),
    #path('ajax/<int:pk>', views.cargar_comentarios, name='ejemploajax'),
    #path('panel_noticias', views.PanelNoticias, name='panel_noticias'),
]