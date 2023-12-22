from django.shortcuts import render
from ..noticias.models import Noticia

# Create your views here.
def UltimasNoticias(request):
    contexto = {}
    n = Noticia.objects. all().order_by('-fecha_publicacion')[:9]
    contexto['noticias'] = n
    
    return render (request, 'home.html', contexto)