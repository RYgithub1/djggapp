from django import forms
from .models import Club, Department



class SearchForm(forms.Form):
  club = forms.ModelChoiceField(
    queryset = Club.objects,
    label = 'CLUB',
    required = False,
  )

  Department = forms.ModelChoiceField(
    queryset = Department.objects,
    label = 'DEPARTMENT',
    required = False,
  )