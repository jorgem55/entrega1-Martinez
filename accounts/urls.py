from django.urls import path
from .views import login, signin, profile, edit_profile, ChangePasswordView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('signin/', signin, name='signin'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/change-password/', ChangePasswordView.as_view(), name='change_password'),
]
