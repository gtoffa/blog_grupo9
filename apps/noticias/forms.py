from django import forms
from .models import Noticia
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML
from django.forms import ImageField, FileInput

class NoticiaForm(forms.ModelForm):
    imagenes = ImageField(widget=FileInput,label="Nueva Imagen")
    class Meta:
        model = Noticia
        fields = [
            'titulo',
            'resumen',
            'contenido',
            'imagenes',
            'categoria_noticia',
        ]
        widgets = {
            'titulo': forms.TextInput(),
            'resumen': forms.Textarea(),
            'categoria_noticia': forms.Select(attrs={'class': 'form-control'}),
            'imagenes': forms.ClearableFileInput(attrs={'class': 'form-control', 'label': 'Nueva Etiqueta'}),
        }


    def __init__(self, *args, **kwargs):
        super(NoticiaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-group'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            'titulo',
            'resumen',
            'categoria_noticia',
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
            'imagenes',
            'contenido',
        )
