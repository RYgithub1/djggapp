from django.db import models
from django.urls import reverse



CHOICES = (('bbc','BBC'),('cnn','CNN'),('dw','DW'),('nhk','NHK')) # TUPLE
class Book(models.Model):
  title = models.CharField(max_length=100)
  text = models.TextField(blank=True, null=True)
  content = models.TextField(default='AROUSAL')
  author = models.CharField(max_length=20, default='ANONYMOUS')
  company = models.CharField(max_length=20, choices=CHOICES, default='DW')

  def __str__(self):
    return self.title # obj.save() create obj in views.py||AdminSite. -> Show it on admin __str__.

  def save(self, *args, **kwargs):
    '''
    self.title = 'ANONYMOUS'
    self.text = 'ANONYMOUS'
    self.content = 'ANONYMOUS'
    self.author = 'ANONYMOUS'
    self.company = 'ANONYMOUS'
    '''
    super(Book, self).save(*args, **kwargs) # SAVE button happens this save method.

  def get_absorute_url(self):
    ## FOR ABSOLUTE PATH
    # return '/detail/%i' % self.id   ## %i=pk number.
    # return reverse('detail', args=[(self.id)])
    ## FOR REDIRECT TEST
    return '/admin/'
    # return '/book/page/'
    # return ''



class FileUpload(models.Model):
  files = models.FileField()
