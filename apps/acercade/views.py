from django.shortcuts import render, redirect
from .models import InformacionContacto
# Asegúrate de tener un archivo forms.py en tu aplicación
from .forms import InformacionContactoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def formulario_contacto(request):
    if request.method == 'POST':
        form = InformacionContactoForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes redirigir a una página de éxito o a donde desees
            return redirect('acercade:exito')
    else:
        form = InformacionContactoForm()

    return render(request, 'acercade/acercade.html', {'form': form})
# esto es para el exito al subir el contacto


def exito(request):
    return render(request, 'acercade/exito.html')


@login_required
def mensajes(request):
    if request.user.is_staff == False:
        return redirect('home:inicio')
    contexto = {}
    n = InformacionContacto.objects.all().order_by('-fecha_creado')
    page = request.GET.get('page', 1)
    # Crear un objeto Paginator
    registros_por_pagina = 10
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
        'mensajes': n,
        'registros': registros_pagina_actual,
        'total_registros': total_registros,
        'total_paginas': total_paginas,
        'page': page,

    }
    return render(request, 'acercade/mensajes.html', contexto)
