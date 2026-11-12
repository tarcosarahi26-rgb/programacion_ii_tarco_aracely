from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from catalogo.models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'categoria', 'isbn']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if titulo:
            titulo = titulo.strip()
            if not titulo:
                raise ValidationError('El título no puede estar vacío.')
        return titulo

    def clean_fecha_publicacion(self):
        fecha_publicacion = self.cleaned_data.get('fecha_publicacion')
        if fecha_publicacion and fecha_publicacion > timezone.localdate():
            raise ValidationError('La fecha de publicación no puede ser futura.')
        return fecha_publicacion

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn:
            return isbn
        if len(isbn) != 13 or not isbn.isascii() or not isbn.isdigit():
            raise ValidationError('El ISBN debe tener 13 dígitos y ser numérico.')
        return isbn
    
    