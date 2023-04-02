from django import forms
from .models import JournalComment



class CommentCreatForm(forms.ModelForm):

  class Meta:
    model = JournalComment
    # fields = '__all__'
    fields = ('name', 'text')
