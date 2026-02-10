from django.shortcuts import render, redirect
from django.contrib.auth import login as logIN, authenticate, logout as logOUT
from .forms import LoginForm, RegisterForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        context = {"title":"Аккаунт"}
        return render(request, 'account/index.html', context)
    else:
        return redirect('login')


def login(request):
    form = LoginForm(data=request.POST or None)
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                logIN(request, user)
                return redirect('home')
    return render(request, 'account/login.html', {'form':form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            logIN(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form':form})


def logout(request):
    logOUT(request)
    return redirect('home')
