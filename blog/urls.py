from django.urls import path
from .views import index,members

urlpatterns = [
    path('', index),
    path('index/', index, name='index'),
    path('members/', members, name='members'),
]