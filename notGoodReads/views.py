from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Usuario
from .forms import LivroForm, UsuarioForm


def livro_list(request):
    livros = Livro.objects.all()
    context = {'livro_list': livros}
    return render(request, "notGoodReads/book_list.html", context)


def livro_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = LivroForm()
        else:
            livro = get_object_or_404(Livro, pk=id)
            form = LivroForm(instance=livro)
        return render(request, "notGoodReads/book_registration.html", {'form': form})
    else:
        if id == 0:
            form = LivroForm(request.POST)
        else:
            livro = get_object_or_404(Livro, pk=id)
            form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
        return redirect('/livro/list')


def livro_delete(request, id):
    livro = get_object_or_404(Livro, pk=id)
    livro.delete()
    return redirect('/livro/list')


def usuario_list(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios_list': usuarios}
    return render(request, "notGoodReads/user_list.html", context)


def usuario_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UsuarioForm()
        else:
            usuario = get_object_or_404(Usuario, pk=id)
            form = UsuarioForm(instance=usuario)
        return render(request, "notGoodReads/user_signup.html", {'form': form})
    else:
        if id == 0:
            form = UsuarioForm(request.POST)
        else:
            usuario = get_object_or_404(Usuario, pk=id)
            form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('/usuario/list')


def usuario_delete(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    usuario.delete()
    return redirect('/usuario/list')
