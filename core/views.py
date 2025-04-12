from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import *
from core.serializers import *


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):#primary key
        post = self.get_object()  # id ile post objesini al
        comments = post.comments.all()  # related_name sayesinde
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Album.objects.all()
        return Album.objects.filter(user).order_by('-created_at')

    def perform_create(self, serializer):#o anki kullanıcıyı atamak için yaptık
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def photos(self, request, pk=None):
        album = self.get_object()
        photos = album.photos.all()  # related_name='photos' olduğu için
        serializer = PhotoSerializer(photos, many=True, context={'request': request})
        return Response(serializer.data)


class PhotoViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.none()

    def get_queryset(self):
        album_user = self.request.user
        if album_user.is_staff:
            return Photo.objects.all()
        return Photo.objects.filter(album_user).order_by('-created_at')

class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    @action(detail=True, methods=['get'])
    def todos(self):
        queryset = self.get_queryset().filter(is_completed=True)
        serialize = self.get_serializer(queryset, many=True)
        return Response(serialize.data)

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        user = self.get_object()
        posts = Post.objects.filter(user=user)
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def albums(self, request, pk=None):
        user = self.get_object()
        albums = Album.objects.filter(user=user)
        serializer = AlbumSerializer(albums, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def todos(self, request, pk=None):
        user = self.get_object()
        todos = Todo.objects.filter(user=user)
        serializer = TodoSerializer(todos, many=True, context={'request': request})
        return Response(serializer.data)


