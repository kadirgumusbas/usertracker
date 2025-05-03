from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


User = settings.AUTH_USER_MODEL

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='photos/',blank=True,null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='todos')
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#user
class Geo(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return f'{self.lat},{self.lng}'

class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=30)
    geo = models.OneToOneField(Geo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street}, {self.city}"

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30)
    website = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True, blank=True)
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.name


