from django.db import models
from django.utils import timezone



class Day(models.Model):
  title = models.CharField('TITLE', max_length=200)
  text = models.TextField('TEXT')
  date = models.DateTimeField('DATE', default=timezone.now)

  def __str__(self):
    return self.title
