from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from .forms import MyUserCreationForm, MyUserEditForm
from accounts.models import MoreUserInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'))
            if user is not None:
                django_login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index', 'Success login')
        else:
            return render(request, 'accounts/signin.html', {'form': form}, 'Unsuccess login')
    
    form = MyUserCreationForm()
    return render(request, 'accounts/signin.html', {'form': form}, 'You must be login')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def edit_profile(request):
    user = request.user
    more_user_info, _ = MoreUserInfo.objects.get_or_create(user=user)
    if request.method == 'POST':
        form = MyUserEditForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name')
                
            user.email = data.get('email') if data.get('email') else user.email
            more_user_info.avatar = data.get('avatar') if data.get('avatar') else more_user_info.avatar
            more_user_info.save()
            user.save()
            return redirect('profile')
        else:
            return render(request, 'accounts/edit_profile.html', {'form': form})
            
    form = MyUserEditForm(
        initial={
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'avatar': more_user_info.avatar
        })

    return render(request, 'accounts/edit_profile.html', {'form': form})


class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = '/accounts/profile/'