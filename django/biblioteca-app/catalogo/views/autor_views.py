from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from catalogo.models import Autor
from catalogo.forms.autor_form import AutorForm

from django.contrib.auth.decorators import login_required, permission_required
@login_required

@permission_required('catalogo.view_autor', raise_exception=True)
def autor_list(request):
    pista = request.GET.get('pista', '').strip()
    autor_id = request.GET.get('autor_id', '').strip()
    autores = Autor.objects.all()

    if pista:
        autores = autores.filter(
            Q(nombre__icontains=pista)
            | Q(apellido__icontains=pista)
            | Q(nacionalidad__icontains=pista)
        )
    if autor_id:
        autores = autores.filter(pk=autor_id)

    return render(
        request,
        'autores/libros/autor_list.html',
        {
            'autores': autores,
            'todos_autores': Autor.objects.all(),
            'pista': pista,
            'autor_id': autor_id,
        },
    )

@login_required
@permission_required('catalogo.add_autor', raise_exception=True)
def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado  correctamente.')
            return redirect('autor_list')
    else:
        form = AutorForm()

    return render(
        request,
        'autores/libros/formulario.html',
        {'form': form},
    )

@login_required
@permission_required('catalogo.change_autor', raise_exception=True)
def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor actualizado correctamente.')
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)

    return render(
        request,
        'autores/libros/formulario.html',
        {'form': form},
    )
@login_required
@permission_required('catalogo.delete_autor', raise_exception=True)
def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        try:
            autor.delete()
        except ProtectedError:
            messages.error(request, 'No se puede eliminar la categoría porque tiene libros asociados.')
            return redirect('autor_list')
        else:
            messages.success(request, 'Categoría eliminada correctamente.')
            return redirect('autor_list')

    return render(
        request,
        'autores/libros/autor_confirm_delete.html',
        {'autor': autor},
    )