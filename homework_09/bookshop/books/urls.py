from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about),
    path('list/', views.BooksList.as_view(), name='book_list'),
    path('book_detail/<int:pk>', views.BooksDetail.as_view(), name='book_detail'),

]