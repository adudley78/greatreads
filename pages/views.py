from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book

def index(request):
    books = Book.objects.order_by('-add_date')

    context = {
        'books': books
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def featured(request):
    return render(request, 'pages/featured.html')
