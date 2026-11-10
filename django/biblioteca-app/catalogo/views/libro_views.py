from django.shortcuts import get_object_or_404, redirect, render
from catalogo.models import Libro
from catalogo.forms.libro_form import LibroForm


def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'libros/libros_list.html', {'libros': libros})

def create_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 'libros/formulario.html', {'form': form})    
def update_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/formulario.html', {'form': form})


def delete_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request, 'libros/confirm_delete.html', {'libro': libro})
