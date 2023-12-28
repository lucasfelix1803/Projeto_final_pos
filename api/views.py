from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Post, Todos, Comment
from .serializers import UserSerializer, TodosSerializer, PostSerializer, CommentSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Artistas
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodosViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Albuns
    """
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Músicas
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Músicas
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

