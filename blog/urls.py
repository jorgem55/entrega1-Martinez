from django.urls import path
from .views import index,members,about,contact,add_member,show_member,edit_member,delete_member
from . import views

urlpatterns = [
    path('', index),
    path('index/', index, name='index'),
    path('members/', members, name='members'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    
    path('add_member/', add_member, name='add_member'),
    path('show_member/<int:id>', show_member, name='show_member'),
    path('edit_member/<int:id>', edit_member, name='edit_member'),
    path('delete_member/<int:id>', delete_member, name='delete_member'),
    
    path('posts/', views.ListPosts.as_view(), name='posts'),
    path('add_post/', views.Add_post.as_view(), name='add_post'),
    path('posts/<int:pk>', views.Show_post.as_view(), name='show_post'),
    path('edit_post/<int:pk>', views.Edit_post.as_view(), name='edit_post'),
    path('delete_post/<int:pk>', views.Delete_post.as_view(), name='delete_post'),
    
]