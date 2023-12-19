from django.shortcuts import render, redirect
from .models import InformacionContacto
from .forms import InformacionContactoForm  # Asegúrate de tener un archivo forms.py en tu aplicación

def formulario_contacto(request):
    if request.method == 'POST':
        form = InformacionContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acercade:exito')  # Puedes redirigir a una página de éxito o a donde desees
    else:
        form = InformacionContactoForm()

    return render(request, 'acercade/acercade.html', {'form': form})
#esto es para el exito al subir el contacto
def exito(request):
    return render(request, 'acercade/exito.html')

