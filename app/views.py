from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics

from .models import PerevalAdd
from .serializers import \
    PerevalAddSerializer, \
    PerevalSerializer, \
    PerevalUpdataSerializer


class SubmitData(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalAddSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListData(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UpData(generics.RetrieveUpdateAPIView, generics.GenericAPIView):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalUpdataSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)