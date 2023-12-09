from django import forms
from .models import InformacionContacto

class InformacionContactoForm(forms.ModelForm):
    class Meta:
        model = InformacionContacto
        fields = ['nombre', 'correo', 'telefono', 'mensaje']
