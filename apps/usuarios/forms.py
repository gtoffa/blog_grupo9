from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import Usuario 
from django.forms import ImageField, FileInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML


class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Correo'}),
        label='',
        required=True
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nombre'}),
        label='',
        required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apellido'}),
        label='',
        required=True
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Usuario'}),
        label='',
        required=True
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        label='',
        required=True
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirmar Contraseña'}),
        label='',
        required=True
    )
    # imagen = forms.ImageField(label='Imagen de perfil', required=False)

    class Meta:
        model = Usuario
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]
        


class PerfilForm(UserChangeForm):
    imagenes = ImageField(widget=FileInput, label="Nueva Imagen")
    

    # imagen = forms.ImageField(label='Imagen de perfil', required=False)

    class Meta:
        model = Usuario
        fields = [
            'email', 
            'first_name',
            'last_name',
            'imagenes',
            'password', 
        ]
        

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-group'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            'email',
            'first_name',
            'last_name', 
            'imagenes',
            HTML("""
                {% if form.instance.imagenes %}
                <label for="id_resumen" class=" requiredField">
                Imagen asociada<span class="asteriskField">*</span> </label>
                    <div>
                        <img style="max-width: 500px;" class=" rounded mx-auto d-block img-thumbnail" src="{{ form.instance.imagenes.url }}">
                         
                    </div>
                    <br/>
                {% endif %}
                  
              
            """),
            
        )
