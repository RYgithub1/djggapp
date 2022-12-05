from django.http import HttpResponse
from .models import FileUpload, Book
from django.shortcuts import get_object_or_404, render, redirect
import mimetypes
import shutil
from django.core.paginator import Paginator



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


def indexview(request):
  object_list =Book.objects.all()
  paginator = Paginator(object_list, 4)
  page = request.GET.get('page', 1)
  paginated_list = paginator.page(page)
  return render(request, 'book/index.html', {'paginated_list':paginated_list})


def redirectview(request, pk):
  object = Book.objects.get(pk=pk)
  return redirect(object)