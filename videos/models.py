from django.db import models



class Video(models.Model):
  title = models.CharField('TITLE', max_length=255)
  description = models.TextField('DESCRIPTION (or EMPTY)', blank=True)
  thumbnail = models.ImageField('THUMBNAIL (or EMPTY)', upload_to='thumbnails/', null=True, blank=True)
  upload = models.ImageField('FILE', upload_to='uploads/%Y/%m/%d/')
  created_at = models.DateTimeField('CREATED DATE', auto_now_add=True)
  updated_at = models.DateTimeField('UPDATED DATE', auto_now=True)

  def __str__(self):
    return self.title
