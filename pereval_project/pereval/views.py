from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class UserViewset(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

class PerevalViewset(viewsets.ModelViewSet):
   queryset = Pereval.objects.all()
   serializer_class = PerevalSerializer 
   filter_backends = [DjangoFilterBackend]
   filterset_fields = ['user__email']

   def partial_update(self, request, *args, **kwargs):
      instance = self.get_object()
      if instance.status == 'ne':
         try:
            data = request.data
         
            instance.title = data.get('title')
            instance.other_titles = data.get('other_titles')
            instance.beautyTitle = data.get('beautyTitle')
            instance.status = data.get('status')
            instance.connect = data.get('connect')
            instance.coords.latitude = data['coords']['latitude']
            instance.coords.longitude = data['coords']['longitude']
            instance.coords.height = data['coords']['height']

            instance.save()

            perevalimages = PerevalImages.objects.filter(pereval=instance)
            
            input_images = data['images']

            i = 0
            for input_image in input_images:
               try:
                  image = perevalimages[i].image
                  image.title = input_image['title']
                  image.data = input_image['data']
               except IndexError:
                  new_image = Image.objects.create(title=input_image['title'], data=input_image['data'])
                  PerevalImages.objects.create(image=new_image, pereval=instance)
               
               image.save()
               i += 1

               serializer = self.get_serializer(instance)

            return Response({'state': 1, 'massage': 'ok'})
         except:
            return Response({'state': 0, 'message': 'Bad request'})
      else:
         return Response({'state': 0, 'message': "Status not 'new'"})
      

