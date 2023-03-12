from django.db import models
from django.utils import timezone



class Department(models.Model):
  name = models.CharField('Department Name', max_length=22)
  created_at = models.DateTimeField('Date', default=timezone.now)

  def __str__(self):
    return self.name




class Club(models.Model):
  name = models.CharField('Cclub name', max_length = 33)
  created_at = models.DateTimeField('Date', default=timezone.now)

  def __str__(self):
    return self.name



class Employ(models.Model):
  first_name = models.CharField('first name', max_length=20)
  last_name = models.CharField('last name', max_length=20)
  email = models.EmailField('mail address', blank=True)
  department = models.ForeignKey(
    Department,
    verbose_name = 'department',
    on_delete = models.PROTECT,
  )
  created_at = models.DateTimeField('Date', default=timezone.now)

  def __str__(self):
    return '{0} {1} {2}'.format(self.last_name, self.first_name, self.department)
