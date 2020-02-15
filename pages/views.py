from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book
from readers.models import Reader

def index(request):
    books = Book.objects.order_by('-add_date')

    context = {
        'books': books
    }

    return render(request, 'pages/index.html', context)

def about(request):
    readers = Reader.objects.order_by('join_date')

    top_readers = Reader.objects.all().filter(is_top=True)    

    context = {
        'readers': readers,
        'top_readers': top_readers
    }

    return render(request, 'pages/about.html', context)

def featured(request):
    return render(request, 'pages/featured.html')
