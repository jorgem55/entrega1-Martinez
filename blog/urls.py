from django.urls import path
from .views import index,members,about,contact,add_member, posts,show_member,edit_member,delete_member

urlpatterns = [
    path('', index),
    path('index/', index, name='index'),
    path('members/', members, name='members'),
    path('add_member/', add_member, name='add_member'),
    path('show_member/<int:id>', show_member, name='show_member'),
    path('edit_member/<int:id>', edit_member, name='edit_member'),
    path('delete_member/<int:id>', delete_member, name='delete_member'),
    path('posts/', posts, name='posts'),
    
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]