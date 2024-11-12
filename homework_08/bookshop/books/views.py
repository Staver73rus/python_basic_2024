from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Book

# Create your views here.

def index(request):
    return render(request, 'books/index.html')

def about(request):
    context = {
        "about_info": "Книжный Магазин",
    }
    return render(request, 'books/about.html', context=context)

class BooksList(ListView):
    template_name = 'books/books_list.html'
    model = Book

class BooksDetail(DetailView):
    template_name = 'books/books_detail.html'
    model = Book
