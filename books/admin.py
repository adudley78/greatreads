from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'author', 'reader')
  list_display_links = ('id', 'title')
  list_filter = ('reader',)
  search_fields = ('title', 'author', 'notes')
  list_per_page = 25

admin.site.register(Book, BookAdmin)
