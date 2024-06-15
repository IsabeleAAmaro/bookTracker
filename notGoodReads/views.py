from django.shortcuts import render, redirect
from .models import Livro
from models import Usuario
from models import Genero

# Create your views here.
def livro_list(request):
    context = {'livro_list': Livro.objects.all()}
    return render(request, "notGoodReads/book_registration.html", context)


def usuario_list(request):
    context = {'usuarios_list': Usuario.objects.all()}
    return render(request, "notGoodReads/user_signup.html", context)
