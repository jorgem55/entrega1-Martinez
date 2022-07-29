from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = { key: '' for key in fields }

class MyUserEditForm(forms.Form):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='First name', max_length=20, required=False)
    last_name = forms.CharField(label='Last name', max_length=20, required=False)
    avatar = forms.ImageField(required=False)
