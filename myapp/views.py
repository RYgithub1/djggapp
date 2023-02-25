from django.shortcuts import render #, get_object_or_404, redirect
#from django.http import HttpResponse



def myapp_index(request):
  context = {'name':'Yade'}
  #return HttpResponse("Hello, world")
  return render(request, 'myapp/index.html', context)



def myapp_about(request):
  context = {}
  return render(request, 'myapp/about.html', context)


def myapp_info(request):
  context = {}
  return render(request, 'myapp/info.html', context)
