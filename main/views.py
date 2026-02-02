from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def shop(request):
    return render(request, 'main/shop.html')

def about(request):
    return render(request, 'main/about.html')

def faq(request):
    return render(request, 'main/faq.html')

def blog(request):
    return render(request, 'main/blog.html')

def gallery(request):
    return render(request, 'main/gallery.html')
