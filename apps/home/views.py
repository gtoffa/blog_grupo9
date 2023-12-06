from django.shortcuts import render
from ..noticias.models import Noticia

# Create your views here.
def UltimasNoticias(request):
    contexto = {}
    n = Noticia.objects.all() 
    contexto['noticias'] = n
    
    return render (request, 'home.html', contexto)