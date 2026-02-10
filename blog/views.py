from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"title":"Блог"}
    return render(request, 'blog/index.html', context)
