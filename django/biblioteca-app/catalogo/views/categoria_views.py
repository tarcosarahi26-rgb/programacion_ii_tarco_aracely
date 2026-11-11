from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from catalogo.models import Categoria
from catalogo.forms.categoria_form import CategoriaForm
from django.contrib.auth.decorators import login_required, permission_required
@login_required

@permission_required('catalogo.view_categoria', raise_exception=True)
def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        'catalogo/categorias/categorias_list.html',
        {'categorias': categorias},
    )

@login_required
@permission_required('catalogo.add_categoria', raise_exception=True)
def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada correctamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm()

    return render(
        request,
        'catalogo/categorias/formulario.html',
        {'form': form},
    )

@login_required
@permission_required('catalogo.change_categoria', raise_exception=True)
def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada correctamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)

    return render(
        request,
        'catalogo/categorias/formulario.html',
        {'form': form},
    )
@login_required
@permission_required('catalogo.delete_categoria', raise_exception=True)
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        try:
            categoria.delete()
        except ProtectedError:
            messages.error(request, 'No se puede eliminar la categoría porque tiene libros asociados.')
            return redirect('categoria_list')
        else:
            messages.success(request, 'Categoría eliminada correctamente.')
            return redirect('categoria_list')

    return render(
        request,
        'catalogo/categorias/categoria_confirm_delete.html',
        {'categoria': categoria},
    )