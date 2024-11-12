from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'books/index.html')

def about(request):
    context = {
        "about_info": "Книжный Магазин",
    }
    return render(request, 'books/about.html', context=context)