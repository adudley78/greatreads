from django.contrib import admin

from .models import Reader

class ReaderAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'join_date')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 25

admin.site.register(Reader, ReaderAdmin)
