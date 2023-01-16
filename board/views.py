from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Board
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



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
        # return render(request, 'board/login.html', {'logincheck': 'LOGED IN.'})
        return redirect('snslistfunc')
    else:
        # return render(request, 'board/login.html', {'logincheck': 'COULD NOT LOG IN.'})
        return render(request, 'board/login.html', {})
  # return render(request, 'board/login.html', {'logincheck': 'IT WAS GET METHOD.'})
  return render(request, 'board/login.html', {})



@login_required
def snslistfunc(request):
  sns_list = Board.objects.all()
  return render(request, 'board/snslist.html', {'sns_list': sns_list})



def logoutfunc(request):
    logout(request)
    return redirect('loginfunc')