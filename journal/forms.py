from django import forms
from .models import JournalComment



class CommentCreateForm(forms.ModelForm):

  class Meta:
    model = JournalComment
    # fields = '__all__'
    fields = ('name', 'comment')
