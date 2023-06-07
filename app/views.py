import django_filters.rest_framework
from rest_framework import mixins, generics
from rest_framework.exceptions import ValidationError

from .models import PerevalAdd, User
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


class UpData(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalUpdataSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status != 'new':
            raise ValidationError("This entry has already been taken for moderation")
        else:
            return self.partial_update(request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalAddSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]