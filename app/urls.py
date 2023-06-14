from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SubmitData, ListData, UpData, UserList


urlpatterns = [
    path('new/', SubmitData.as_view(), name='new'),
    path('<int:pk>/', ListData.as_view(), name='id'),
    path('edit/<int:pk>/', UpData.as_view(), name='edit'),
    path('filter/', UserList.as_view(), name='filter'),
]