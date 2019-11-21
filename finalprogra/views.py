from django.shortcuts import render
from django.contrib import messages
from .forms import MenuForm
from menus.models import Menu, Plato, Comida
# Create your views here.

def menu_nueva(request):
    if request.method == "POST":
        formulario = MenuForm(request.POST)
        if formulario.is_valid():
             menu = Menu.objects.create(nombre=formulario.cleaned_data['nombre'], total = formulario.cleaned_data['total'])
             for plato_id in request.POST.getlist('platos'):
                 comida = Comida(plato_id=plato_id, menu_id = menu.id)
                 comida.save()
             messages.add_message(request, messages.SUCCESS, 'Guardado Exitosamente')
    else:
        formulario = MenuForm()
    return render(request, 'menus/editar.html', {'formulario': formulario})
