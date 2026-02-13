from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"title":"Галерея"}
    return render(request, 'gallery/index.html', context)
