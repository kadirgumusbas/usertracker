from rest_framework import serializers
from core.models import *



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, data):
        #albüm giriş yapana mı ait
        album = data.get('album')
        request = self.context.get('request')

        if album.user != request.user:
            raise serializers.ValidationError("Bu albüm size ait değil")

        return data

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

    def validate(self, data):
        album = data.get('album')
        request = self.context.get('request')

        if album.user != request.user:
            raise serializers.ValidationError("Bu albüm size ait değil.")
        return data

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ['lat', 'lng']

class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()

    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode', 'geo']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()

    class Meta:
        model = CustomUser
        fields = [
            'id', 'name', 'username', 'email','address',
            'phone', 'website',
            'company',
        ]






