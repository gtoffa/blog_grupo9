from django.shortcuts import render, redirect
from .models import Noticia, Categoria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count , Q
from django.db.models.functions import TruncYear, TruncMonth
from django.urls import reverse
from datetime import datetime
# Create your views here.


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
         n = n.filter(Q(titulo__icontains=buscar) | Q(contenido__icontains=buscar))
         
    if archivo:
      
        try:
            fecha_objeto = datetime.strptime(archivo, '%m-%Y').date()
            
    
        except ValueError:
            fecha_objeto = None
        
        if fecha_objeto:
                n = n.filter(fecha_publicacion__month=fecha_objeto.month, fecha_publicacion__year=fecha_objeto.year)  

    if antiguedad:
        if antiguedad == "asc":
            n = n.order_by('fecha_publicacion')
        elif antiguedad == "desc":
            n = n.order_by('-fecha_publicacion')

    if orden:
        if orden == "asc":
            n = n.order_by('titulo')
        elif orden == "desc":
            n = n.order_by('-titulo')

    # Crear un objeto Paginator
    registros_por_pagina = 1
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
        'archivo':archivo,
        'fecha_objeto':fecha_objeto

    }
    contexto = PanelNoticias(contexto)

    return render(request, 'noticias/listar.html', contexto)


def DetalleNoticia(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk=pk)  # SELECT * FROM NOTICIAS WHERE id = 1

    # actualizar numeros de visitas
    n.cant_vistas = n.cant_vistas + 1
    n.save()

    contexto['noticias'] = n

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
