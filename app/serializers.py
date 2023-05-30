from rest_framework import serializers
from .models import User, Coords, PerevalAdd, Image, Level


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
        fields = ['title_image', 'data']


class PerevalAddSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    image = ImageSerializer()

    class Meta:
        model = PerevalAdd
        fields = [
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'add_time',
            'user',
            'coords',
            'level',
            'image',
        ]

    def create(self, validated_data):
        user_new = validated_data.pop('user')
        user = User.objects.create(**user_new)

        coords_new = validated_data.pop('coords')
        coords = Coords.objects.create(**coords_new)

        level_new = validated_data.pop('level')
        level = Level.objects.create(**level_new)

        image_new = validated_data.pop('image', [])
        image = Image.objects.create(**image_new)

        pereval_add = PerevalAdd.objects.create(**validated_data, user=user, coords=coords, level=level, image=image)

        return pereval_add