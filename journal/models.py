from django.db import models
from django.utils import timezone



class JournalCategory(models.Model):
  name = models.CharField('CATEGORY NAME', max_length=255)
  created_date = models.DateTimeField('CREATED DATE', default=timezone.now)

  def __str__(self):
    return self.name



class JournalPost(models.Model):
  title = models.CharField('TITLE', max_length=255)
  text = models.TextField('TEXT')
  created_date = models.DateTimeField('CREATED DATE', default=timezone.now)

  category = models.ForeignKey(
    JournalCategory,
    verbose_name = 'CATEGORY',
    on_delete = models.PROTECT,
  )

  def __str__(self):
    return self.title
