import threading
from django.shortcuts import get_object_or_404, render, redirect

from apps.noticias.forms import NoticiaForm
from .models import Noticia, Categoria, Comentario
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.db.models.functions import TruncYear, TruncMonth
from django.urls import reverse
from datetime import datetime
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_ajax.decorators import ajax
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
 
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
 

# Create your views here.
# Creamos un objeto local enhebrado para almacenar el usuario actual
thread_local = threading.local()

def get_current_user():
    return getattr(thread_local, 'user', None)

# Definir una función middleware para establecer el usuario actual en cada solicitud
class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        thread_local.user = request.user
        response = self.get_response(request)
        return response

def ListarNoticias(request):
    contexto = {}
    categoria_todos = Categoria(pk=0, nombre='Todas')
    id_categoria = request.GET.get("id", "0")
    antiguedad = request.GET.get("antiguedad", None)
    buscar = request.GET.get("buscar", None)
    orden = request.GET.get("orden", None)
    archivo = request.GET.get("archivo", None)
    page = request.GET.get('page', 1)
    fecha_objeto = None

    n = Noticia.objects.all()

    if id_categoria != "0":
        n = n.filter(categoria_noticia=id_categoria)
        cat = Categoria.objects.get(id=id_categoria)
    else:
        cat = categoria_todos

    if buscar:
        n = n.filter(Q(titulo__icontains=buscar) |
                     Q(contenido__icontains=buscar))

    if archivo:

        try:
            fecha_objeto = datetime.strptime(archivo, '%m-%Y').date()

        except ValueError:
            fecha_objeto = None

        if fecha_objeto:
            n = n.filter(fecha_publicacion__month=fecha_objeto.month,
                         fecha_publicacion__year=fecha_objeto.year)

    if antiguedad:
        if antiguedad == "asc":
            n = n.order_by('fecha_publicacion')
        elif antiguedad == "desc":
            n = n.order_by('-fecha_publicacion')
    else:
        n = n.order_by('-fecha_publicacion')

    if orden:
        if orden == "asc":
            n = n.order_by('titulo')
        elif orden == "desc":
            n = n.order_by('-titulo')

    # Crear un objeto Paginator
    registros_por_pagina = 3
    paginator = Paginator(n, registros_por_pagina)
    # Obtener el número de página desde la solicitud GET

    try:
        # Obtener la página actual
        registros_pagina_actual = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número entero, mostrar la primera página
        registros_pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, mostrar la última página
        registros_pagina_actual = paginator.page(paginator.num_pages)

    # Obtener la cantidad total de registros
    total_registros = paginator.count

    # Calcular la cantidad total de páginas
    total_paginas = paginator.num_pages

    contexto = {
        'noticias': n,
        'registros': registros_pagina_actual,
        'total_registros': total_registros,
        'total_paginas': total_paginas,
        'categoria_select': cat,
        'orden': orden,
        'antiguedad': antiguedad,
        'page': page,
        'buscar': buscar,
        'archivo': archivo,
        'fecha_objeto': fecha_objeto

    }
    contexto = PanelNoticias(contexto)

    return render(request, 'noticias/listar.html', contexto)


def DetalleNoticia(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk=pk)  # SELECT * FROM NOTICIAS WHERE id = 1
    c = n.comentarios.all()
    # actualizar numeros de visitas
    n.cant_vistas = n.cant_vistas + 1
    n.save()

    contexto = {
        'noticias': n,
        'comentarios': c,
    }

    contexto = PanelNoticias(contexto)

    id_categoria = request.GET.get("id", None)
    archivo = request.GET.get("archivo", None)
    redirect_url = reverse('noticias:listar')
    
    if id_categoria is not None:
        redirect_url += f'?id={id_categoria}'
        return redirect(redirect_url)
    elif archivo is not None:
        redirect_url += f'?archivo={archivo}'
        return redirect(redirect_url)
    else:
        return render(request, 'noticias/detalle.html', contexto)


def Ultmias10Noticias(request):
    contexto = {}
    n = Noticia.objects. all().order_by('-fecha_publicacion')[:10]


def PanelNoticias(contexto):
    categoria_todos = Categoria(pk=0, nombre='Todas')
    # Categorias disponibles

    cat = []
    cat.append(categoria_todos)
    # ordena por nombre
    cat.extend(list(Categoria.objects.all().order_by('nombre')))

    contexto['categorias'] = cat

    # Top Noticias
    n = Noticia.objects. all().order_by('-cant_vistas')[:3]
    contexto['popular_noticias'] = n

    resumen_noticias = (
        Noticia.objects
        .annotate(month=TruncMonth('fecha_publicacion'))
        .values('month')
        .annotate(cant_noticias=Count('id'))
    )

    # Formatear y mostrar el resumen
    contexto['resumen_noticias'] = resumen_noticias

    return contexto


@ajax
@login_required
def cargar_comentarios(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    contexto = {}
    if request.method == 'POST':
        # Obtener el contenido del comentario desde la solicitud POST
        comentario_contenido = request.POST.get('contenido', '')
        id_comentario = request.POST.get('id_comentario', '')
        id_comentario = int(id_comentario) if id_comentario.strip() else 0
        usuario = request.user

        # Verificar si el comentario no está vacío
        if not comentario_contenido:
            return JsonResponse({'error': 'El comentario no puede estar vacío'}, status=400)

        # Lógica para crear un comentario en la base de datos
        if id_comentario == 0:
            Comentario.objects.create(
                noticia=noticia, usuario=usuario, contenido=comentario_contenido)
        else:
            comentario = get_object_or_404(Comentario, id=id_comentario)
            comentario.contenido=comentario_contenido
            comentario.save()

        c = noticia.comentarios.all()
        contexto = {
            'comentarios': c,
            'user': usuario
        }

        comentario_html = render_to_string(
            'noticias/comentarios.html', contexto)

        return HttpResponse(comentario_html)
    return JsonResponse({'error': 'Solicitud no válida'}, status=400)


@ajax
@login_required
def eliminar_comentarios(request, id_comentario):
    comentario = get_object_or_404(Comentario, id=id_comentario)
    contexto = {}
    if request.method == 'GET':
        # Obtener el contenido del comentario desde la solicitud POST

        usuario = request.user
        id = comentario.noticia.pk
        if comentario.usuario == request.user or usuario.is_staff:
            comentario.delete()

        noticia = get_object_or_404(Noticia, id=id)  
        c = noticia.comentarios.all()
        contexto = {
            'comentarios': c,
            'user': usuario
        }

        comentario_html = render_to_string(
            'noticias/comentarios.html', contexto)

        return HttpResponse(comentario_html)
    return JsonResponse({'error': 'Solicitud no válida'}, status=400)


@login_required
def AddNoticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST or None, request.FILES) ##Request files es para las imagenes

        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            form.save()
            redirect_url = reverse('noticias:listar')
            return redirect(redirect_url) 
    else:
        form = NoticiaForm()
    
    return render (request, 'noticias/addNoticia.html', {'form':form})

@login_required
def EditarNoticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    content_type = ContentType.objects.get_for_model(noticia)
    # Obtener las entradas de historial de cambios para tu modelo
    history_entries = LogEntry.objects.filter(content_type=content_type, object_id = pk).order_by('-action_time')[:10]


    # Solo el autor puede editar la noticia
    if noticia.autor != request.user:
        return HttpResponseForbidden("No tenes permiso para editar esta noticia.")

    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticias:detalle', pk=pk)
    else:
        form = NoticiaForm(instance=noticia)

    context = {
        'form': form,
        'history':history_entries,
        'user': request.user
    }
    return render(request, 'noticias/editar.html', context)