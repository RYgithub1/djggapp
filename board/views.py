from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User



def qwerty(request):
  return HttpResponse('RESPONSED')


def signupfunc(request):
  ## object_list = User.objects.all()
  # object = User.objects.get(username='djgguser')
  if request.method == 'POST':
    # print(request.POST) # FORM INPUT DATA -> MAKE AN USER.
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username, '', password)

  else:
    print('-------------- NOT POST')


  return render(request, 'board/signup.html', {'some': 11100})
