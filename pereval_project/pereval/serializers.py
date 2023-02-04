from pereval.models import *
from rest_framework import serializers

class CoordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coords
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PerevalUser
        fields = '__all__'

class ImageSerialize(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['data', 'title']

class PerevalSerializer(serializers.ModelSerializer):

    coords = CoordsSerializer()
    user = UserSerializer()
    images = ImageSerialize(many=True)

    class Meta:

        model = Pereval
        fields = ['title', 'other_titles', 'beautyTitle', 'connect', 'status', 'user', 'coords', 'images']
    
    def create(self, validated_data):

        coords_data = validated_data.pop('coords')
        user_data = validated_data.pop('user')
        images_data = validated_data.pop('images')

        coords = Coords.objects.create(**coords_data)
        user = PerevalUser.objects.create(**user_data)
        pereval = Pereval.objects.create(coords=coords, user=user, **validated_data)

        for image_data in images_data:
            image = Image.objects.create(**image_data)
            PerevalImages.objects.create(pereval=pereval, image=image)
        
        pereval.save()

        return pereval