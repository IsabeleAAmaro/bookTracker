from django import forms
from .models import Livro, Usuario


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('titulo', 'autor', 'status_leitura', 'genero', 'usuario', 'isbn')  # 'isbn' minúsculo
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'status_leitura': 'Status de Leitura',
            'genero': 'Gênero',
            'usuario': 'Usuário',
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


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'senha')
        labels = {
            'username': 'Nome de Usuário',
            'email': 'Email',
            'senha': 'Senha'
        }

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].empty_label = "Select"
        self.fields['email'].empty_label = "Select"
        self.fields['senha'].empty_label = "Select"
