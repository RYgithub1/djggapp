from django.db import models



class Book(models.Model):
  title = models.CharField(max_length=100)
  text = models.TextField(blank=True, null=True)
  content = models.TextField(default='AROUSAL')
  author = models.CharField(max_length=20, default='ANONYMOUS')

