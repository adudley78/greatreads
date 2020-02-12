from django.db import models
from datetime import datetime
from readers.modles import Reader

class Model(models.Model):
  reader = models.ForeignKey(Reader, on_delete=models.DO_NOTHING)
  title: models.CharField(max_length=200)
  author: models.CharField(max_length=200)
  genre: models.CharField(max_length=200)
  notes: models.TextField(blank=True)
  has_read: models.BooleanField(default=True)
  add_date: models.DateTimeField(default=datetime.now, blank=True)
  cover_img: models.ImageField(upload_to='covers')
  def __str__(self):
    return self.title
