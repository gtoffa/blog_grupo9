from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from apps.usuarios.models import Usuario
from .forms import PerfilForm, RegistroForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from ..noticias.models import Noticia , Comentario
# LOGIN


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:inicio')
        else:
            messages.error(request, 'Usuario o contraseña invalidos')

    return render(request, 'usuarios/login.html')

# Cerrar sesion


def user_logout(request):
    logout(request)
    return redirect('usuarios:login')

# Crear cuenta


class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('usuarios:login')
    template_name = 'usuarios/registro.html'


@login_required
def Perfil(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    if user != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este perfil.")



    
    
    n = Noticia.objects.filter(autor=user).all().order_by('-fecha_publicacion')[:5]
    c = Comentario.objects.filter(usuario=user).all().order_by('-fecha_creacion')[:5]
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            
            form.save()
            return redirect('noticias:listar')
    else:
        form = PerfilForm(instance=user)

    context = {
        'form': form,
        'user': request.user,
        'posteos':n,
        'comentarios':c,
    }
    return render(request, 'usuarios/perfil.html', context)