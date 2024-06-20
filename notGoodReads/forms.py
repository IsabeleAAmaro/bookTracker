from django import forms
from .models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('titulo', 'autor', 'status_leitura', 'genero', 'usuario', 'ISBN')
        labels = {
            'titulo': 'Titulo',
            'autor': 'Autor',
            'status_leitura': 'Status',
            'genero': 'Genero',
            'usuario': 'Usuario',
            'isbn': 'ISBN'
        }

    def __init__(self, *args, **kwargs):
        super(LivroForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].empty_label = "Select"
        self.fields['autor'].empty_label = "Select"
        self.fields['status_leitura'].empty_label = "Select"
        self.fields['genero'].empty_label = "Select"
        self.fields['usuario'].empty_label = "Select"
        self.fields['isbn'].empty_label = "Select"
