from django.shortcuts import render
from django.db.models import Q
from .models import Grupo
from .forms import SearchForm

def lista_grupos(request):
    form = SearchForm(request.GET or None)
    grupos = Grupo.objects.all()
    hay_resultados = True
    if form.is_valid() and request.GET:
        tipo_retiro = form.cleaned_data.get('tipo_retiro')
        ciudad = form.cleaned_data.get('ciudad')
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_final = form.cleaned_data.get('fecha_final')

        if tipo_retiro:
            grupos = grupos.filter(nombre__icontains=tipo_retiro)
        if ciudad:
            grupos = grupos.filter(ciudad=ciudad)
        if fecha_inicio and fecha_final:
            grupos = grupos.filter(
                Q(fecha_inicio__lte=fecha_final) & Q(fecha_fin__gte=fecha_inicio)
            )
            
        if not grupos.exists():  # Si no hay grupos después de filtrar
            hay_resultados = False
            
        
    return render(request, 'index.html', {
        'form': form,
        'grupos': grupos,
        'hay_resultados': hay_resultados  # Pasa la variable a la plantilla
    })
    
def about(request):
    return render(request, 'about.html')
