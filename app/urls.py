from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SubmitData, ListData, UpData, UserList


urlpatterns = [
    path('new/', SubmitData.as_view()),
    path('<int:pk>/', ListData.as_view()),
    path('edit/<int:pk>/', UpData.as_view()),
    path('filter/', UserList.as_view()),
]