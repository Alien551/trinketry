from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    context = {"title":"Корзина"}
    return render(request, 'cart/index.html')


def add_to_cart(request):
    pass
