from django.db import models

class post(models.Model):
    userid = models.ForeignKey(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=100)


class todos(models.Model):
    userid = models.ForeignKey(max_length=100)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(max_length=100)

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


