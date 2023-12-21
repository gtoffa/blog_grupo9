
from django import forms
from .models import InformacionContacto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Column


class InformacionContactoForm(forms.ModelForm):
    correo = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Correo', 'class': 'form-control'}),
        label='',
        required=True
    )
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Nombre', 'class': 'form-control'}),
        label='',
        required=True
    )
    telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Telefono', 'class': 'form-control'}),
        label='',
        required=False
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Mensaje', 'class': 'form-control'}),
        label='',
        required=True
    )

    class Meta:
        model = InformacionContacto
        fields = ['nombre', 'correo', 'telefono', 'mensaje']

    def __init__(self, *args, **kwargs):
        super(InformacionContactoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'contact-form-data'
        self.helper.form_class = 'contact-form'
        self.helper.form_method = 'post'
        self.helper.form_tag = True

        self.helper.layout = Layout(
            'nombre',
            'correo',
            'telefono',
            'mensaje'
        )
