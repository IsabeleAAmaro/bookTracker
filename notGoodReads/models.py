from django.db import models


# Create your models here.1

class Genero(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=15)


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    status_leitura = models.CharField(max_length=15)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
