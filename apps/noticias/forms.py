from django import forms
from .models import Noticia
from ckeditor.widgets import CKEditorWidget


class NoticiaForm(forms.ModelForm):

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

    'titulo': forms.TextInput(attrs={'class': 'form-control'}),
    'resumen': forms.Textarea(attrs={'class': 'form-control'}),
    'imagenes': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    'categoria_noticia': forms.Select(attrs={'class': 'form-control'}),
}
