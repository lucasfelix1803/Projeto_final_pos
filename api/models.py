from django.db import models


class Artista(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    ano_criacao = models.IntegerField()


def __str__(self):
    return self.nome


class post(models.Model):
    userid = models.ForeignKey(max_length=100)
    id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=100)


class todos(models.Model):
    userid = models.ForeignKey(max_length=100)
    id = models.CharField(max_length=100)    
    title = models.CharField(max_length=100)
    completed = models.BooleanField(max_length=100)