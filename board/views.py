from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login



def signupfunc(request):
  # object_list = User.objects.all()
  # object = User.objects.get(username='djgguser')

  if request.method == 'POST':
    print("request.method == 'POST'")
    ## FORM INPUT DATA -> MAKE AN USER.
    ## Need name-value of InputTag in FormTag to get each data.
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    try:
      user = User.objects.create_user(username, '', password)
      print('Registered newly.')
      return render(request, 'board/signup.html', {'IntegrityErrorCheck': 'Registered newly.'})
    except IntegrityError:
      print('This user is already registered.')
      return render(request, 'board/signup.html', {'IntegrityErrorCheck': 'This user is already registered.'})
  else:
    print("request.method == 'GET'")

  return render(request, 'board/signup.html', {'some': 11100})



def loginfunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'board/login.html', {'logincheck': 'LOGED IN.'})
    else:
        return render(request, 'board/login.html', {'logincheck': 'COULD NOT LOG IN.'})
  return render(request, 'board/login.html', {'logincheck': 'IT WAS GET METHOD.'})
