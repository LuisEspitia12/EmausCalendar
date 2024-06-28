from django.shortcuts import render
from .models import Grupo, Ciudad

def lista_grupos(request):
    grupos = Grupo.objects.all()
    ciudades = Ciudad.objects.all()
    return render(request, 'index.html', {'grupos': grupos, 'ciudades': ciudades})
