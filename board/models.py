from django.db import models



class Board(models.Model):
  snsTitle = models.CharField(max_length=100)
  snsContent = models.TextField()
  snsAuthor = models.CharField(max_length=50)
  snsImage = models.ImageField(upload_to='')
  snsGood = models.IntegerField()
  snsRead = models.IntegerField()
  personsWhoRead = models.TextField()

  def __str__(self):
    return self.snsTitle