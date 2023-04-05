from django import forms
from .models import JournalComment



class CommentCreateForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for a_field in self.fields.values():
      a_field.widget.attrs['class'] = 'form-control'


  class Meta:
    model = JournalComment
    # fields = '__all__'
    fields = ('name', 'comment')
