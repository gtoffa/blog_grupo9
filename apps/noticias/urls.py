from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.ListarNoticias, name='listar'),
    path('detalle/<int:pk>', views.DetalleNoticia, name='detalle'), 
    path('addNoticia', views.AddNoticia, name='addnoticia'),
    path('noticias/<int:pk>/edit/', views.EditarNoticia, name='edit_noticia'),
    path('detalle/ajax/cargar_comentarios/<int:noticia_id>/', views.cargar_comentarios, name='cargar_comentarios'),
    path('detalle/ajax/eliminar_comentarios/<int:id_comentario>/', views.eliminar_comentarios, name='eliminar_comentarios'),
    #path('ajax/<int:pk>', views.cargar_comentarios, name='ejemploajax'),
    #path('panel_noticias', views.PanelNoticias, name='panel_noticias'),
]