'''
Validate input data easily, comparing to views.
'''

from django import forms
from .models import Day



class DayCreateForm(forms.ModelForm):  # OR forms.Form

  class Meta:
    model = Day
    fields = '__all__'  # OR ('title', 'text', 'date')
