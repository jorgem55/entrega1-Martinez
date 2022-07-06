from django.urls import path
from .views import index,members,about,contact,add_member

urlpatterns = [
    path('', index),
    path('index/', index, name='index'),
    path('members/', members, name='members'),
    path('add_member/', add_member, name='add_member'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]