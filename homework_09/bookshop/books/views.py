from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Book
from django.urls import reverse

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
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список книг'
        context['book_count'] = Book.objects.count()
        return context

class BooksDetail(DetailView):
    template_name = 'books/books_detail.html'
    model = Book
