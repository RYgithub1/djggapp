from django.http import HttpResponse
from django.shortcuts import render




def qwerty(request):
  return HttpResponse('RESPONSED')


def signupfunc(request):
  if request.method == 'POST':
    print('-------------- POST')
  else:
    print('-------------- NOT POST')
  return render(request, 'board/signup.html', {'some': 100})
