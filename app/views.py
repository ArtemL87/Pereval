from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics

from .models import PerevalAdd
from .serializers import PerevalAddSerializer


class SubmitData(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalAddSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# Create your views here.
