from django.shortcuts import render

from .models import Book

def index(request):
  books = Book.objects.all()

  context = {
    'books': books
  }

  return render(request, 'books/books.html', context)

def book(request):
  return render(request, 'books/book.html')

def search(request):
  return render(request, 'books/search.html')