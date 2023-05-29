from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SubmitData


urlpatterns = [
    path('new/', SubmitData.as_view()),
]