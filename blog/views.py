from django.shortcuts import render

#se borra esta parte porque queda en la carpeta app/home
#def Home(request):
#    return render(request, 'home.html')

def Nosotros(request):
    return render(request, 'nosotros.html')