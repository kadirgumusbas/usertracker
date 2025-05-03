from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from core.models import *
from core.serializers import *


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']  # Burada hangi alanlara filtre yapılabileceğini söylüyoruz

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):#primary key
        post = self.get_object()  # id ile post objesini al
        comments = post.comments.all()  # related_name sayesinde
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']  # Burada hangi alanlara filtre yapılabileceğini söylüyoruz

class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']  # Burada hangi alanlara filtre yapılabileceğini söylüyoruz


    @action(detail=True, methods=['get'])
    def photos(self, request, pk=None):
        album = self.get_object()
        photos = album.photos.all()  # related_name='photos' olduğu için
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)


class PhotoViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['album']  # Burada hangi alanlara filtre yapılabileceğini söylüyoruz


class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']  # Burada hangi alanlara filtre yapılabileceğini söylüyoruz

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        user = self.get_object()
        posts = Post.objects.filter(user=user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def albums(self, request, pk=None):
        user = self.get_object()
        albums = Album.objects.filter(user=user)
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def todos(self, request, pk=None):
        user = self.get_object()
        todos = Todo.objects.filter(user=user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


