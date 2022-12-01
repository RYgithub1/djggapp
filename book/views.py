from django.http import HttpResponse
from .models import FileUpload, Book
from django.shortcuts import get_object_or_404, render
import mimetypes
import shutil



def firstviewfunction(request):
  # print(dir(request))
  return HttpResponse('RESPONSED')


def downloadview(request, pk):
  object = get_object_or_404(FileUpload, pk=pk)
  file = object.files
  name = file.name
  response = HttpResponse(content_type=mimetypes.guess_type(name)[0] or 'application/octet-stream')
  response['Content-Disposition'] = f'attachment; filename={name}'
  shutil.copyfileobj(file, response)
  # return None
  return response


def detailview(request, pk):
  object = get_object_or_404(Book, pk=pk)
  return render(request, 'book/detail.html', {'object':object})
