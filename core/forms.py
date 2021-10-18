from django.db.models import fields
from django.forms import ModelForm, DateInput
from django.forms.models import inlineformset_factory

from core.models import Autor, Libro


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

        widgets = {
            'fecha_publicacion': DateInput(attrs={
                'type': 'date'
            })
        }


LibroFormSet = inlineformset_factory(Autor, Libro, fields='__all__', extra=2)
