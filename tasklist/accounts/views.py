from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate

from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            authenticate(
                username=user.username,
                password=user.password
            )

            if user is not None:
                auth_login(request, user)
                return redirect('/')

    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')
