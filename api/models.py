from django.db import models


class Artista(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    ano_criacao = models.IntegerField()


def __str__(self):
    return self.nome


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    endereço = models.CharField()
    phone = models.CharField(max_length=11)
    websitev = models.CharField()
    company = models.CharField(max_length=255)


def __str__(self):
    return self.name


class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    segundos = models.IntegerField()
