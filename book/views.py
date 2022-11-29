from django.http import HttpResponse



def firstviewfunction(request):
  # print(dir(request))
  return HttpResponse('RESPONSED')