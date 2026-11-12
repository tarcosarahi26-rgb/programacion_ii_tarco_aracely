from django import forms
from django.core.exceptions import ValidationError
from catalogo.models import Autor
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre:
            nombre = nombre.strip()
            if not nombre:
                raise ValidationError('El nombre no puede estar vacío.')
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if apellido:
            apellido = apellido.strip()
            if not apellido:
                raise ValidationError('El apellido no puede estar vacío.')
        return apellido