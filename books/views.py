from django.shortcuts import render

def index(request):
  return render(request, 'books/books.html')

def book(request):
  return render(request, 'books/book.html')

def search(request):
  return render(request, 'books/search.html')