from django import forms



class ImageUploadForm(forms.Form):
  file = forms.ImageField(label='Image file')
