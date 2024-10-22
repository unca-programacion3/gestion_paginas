from django import forms
from django.forms import inlineformset_factory
from .models import Pagina, Seccion


class PaginaForm(forms.ModelForm):
    class Meta:
        model = Pagina
        fields = ['titulo', 'portada']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'portada': forms.FileInput(attrs={'class': 'form-control'}),
        }


class SeccionForm(forms.ModelForm):
    class Meta:
        model = Seccion
        fields = ['titulo', 'tipo_seccion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_seccion': forms.Select(attrs={'class': 'form-control'}),
        }


# Crear el formset para las secciones
SeccionFormSet = inlineformset_factory(
    Pagina,
    Seccion,
    form=SeccionForm,
    extra=1,  # Número de formularios vacíos
    can_delete=True  # Permite eliminar secciones
)
