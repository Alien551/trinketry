from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Главная страница")

def shop(request):
    return HttpResponse("Страница магазина")

def about(request):
    return HttpResponse("Страница обо мне")

def faq(request):
    return HttpResponse("Страница с ЧАВО")

def blog(request):
    return HttpResponse("Страница с блогом")

def gallery(request):
    return HttpResponse("Галерея работ")
