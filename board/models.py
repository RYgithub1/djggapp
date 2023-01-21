from django.db import models



class Board(models.Model):
  snsTitle = models.CharField(max_length=100)
  snsContent = models.TextField()
  snsAuthor = models.CharField(max_length=50)
  snsImage = models.ImageField(upload_to='')
  snsGood = models.IntegerField(null='True', blank='True', default='1')
  snsRead = models.IntegerField(null='True', blank='True', default='1')
  personsWhoRead = models.TextField(null='True', blank='True', default='dorami')

  def __str__(self):
    return self.snsAuthor