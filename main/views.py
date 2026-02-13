from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request, 'main/index.html', context)

def about(request):
    context={"title":"Обо мне"}
    return render(request, 'main/about.html', context)

def faq(request):
    context={"title":"Чаво"}
    return render(request, 'main/faq.html', context)
