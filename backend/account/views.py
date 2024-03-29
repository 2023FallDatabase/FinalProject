from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate as auth_authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from .forms import UserRegistrationForm, LoginForm


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth_authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth_login(request, user)
        return redirect('/')
    else:
        return render(request, 'registration/login.html', {'form': LoginForm()})


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return render(request, 'registration/logout.html')


def logout_then_login(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect(reverse('login'))
