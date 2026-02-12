from math import log
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm

# Create your views here.
@login_required
def index(request):
    if request.user.is_authenticated:
        context = {"title":"Аккаунт"}
        return render(request, 'account/index.html', context)


def login(request):
    form = LoginForm(data=request.POST or None)
    if request.user.is_authenticated:
        return redirect('main:index')
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)

                if request.POST.get("next", None):
                    return redirect(request.POST.get("next", None))
                return redirect('main:index')

    return render(request, 'account/login.html', {'form':form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('main:index')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form':form})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('main:index')
