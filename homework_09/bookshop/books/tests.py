from django.test import TestCase
from .models import Book
from django.urls import reverse

# Create your tests here.

class TestApp(TestCase):
    
    def setUp(self):
        self.book = Book.objects.create(title = 'test_book', rating = 90, is_best_selling = True, author = 'test_author')

    def test_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'books/books_list.html')
        self.assertIn('books', response.context)

    def tearDown(self):
        Book.objects.all().delete()
