from django.shortcuts import render, redirect
from django.contrib import messages
from catalogo.forms.categoria_form import CategoriaForm
from catalogo.models import Categoria

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria_list.html', {'categorias': categorias})

def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'formulario.html', {'formulario': form})