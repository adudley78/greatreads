from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Book

def index(request):
  books = Book.objects.order_by('-add_date')

  paginator = Paginator(books, 2)
  page = request.GET.get('page')
  paged_books = paginator.get_page(page)

  context = {
    'books': paged_books
  }

  return render(request, 'books/books.html', context)

def book(request, book_id):
  return render(request, 'books/book.html')

def search(request):
  return render(request, 'books/search.html')