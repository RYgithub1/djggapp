from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User



def qwerty(request):
  return HttpResponse('RESPONSED')


def signupfunc(request):
  ## object_list = User.objects.all()
  object = User.objects.get(username='djgguser')
  print(object)
  print(object.email)



  if request.method == 'POST':
    print('-------------- POST')
  else:
    print('-------------- NOT POST')
  return render(request, 'board/signup.html', {'some': 11100})
