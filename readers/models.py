from django.db import models
from datetime import datetime

class Reader(models.Model):
  name = models.CharField(max_length=200)
  profile_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
  bio = models.TextField(blank=True)
  is_top = models.BooleanField(default=False)
  join_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.name