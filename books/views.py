from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from books.choices import genre_choices

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
  book = get_object_or_404(Book, pk=book_id)

  context = {
    'book': book
  }

  return render(request, 'books/book.html', context)

def search(request):

  context = {
    'genre_choices': genre_choices,
  }

  return render(request, 'books/search.html', context)