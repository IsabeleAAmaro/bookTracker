from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=128)  # Use a mesma largura do Django User model

    def __str__(self):
        return self.username


class Livro(models.Model):
    STATUS_CHOICES = [
        ('Lido', 'Lido'),
        ('Lendo', 'Lendo'),
        ('Quero ler', 'Quero ler'),
    ]

    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    status_leitura = models.CharField(max_length=15, choices=STATUS_CHOICES)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.titulo
