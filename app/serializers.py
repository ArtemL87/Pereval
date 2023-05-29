from rest_framework import serializers
from .models import User, Coords, Pereval, Image, Level


class PerevalSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Pereval
       fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'data']


