from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Board
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy



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



def snsdetailfunc(request, pk):
  object = get_object_or_404(Board, pk=pk)
  return render(request, 'board/snsdetaild.html', {'object': object})



def likeitfunc(request, pk):
  object = Board.objects.get(pk=pk)
  object.snsGood += 1
  object.save()
  return redirect('snslistfunc')


def readitfunc(request, pk):
  object = Board.objects.get(pk=pk)

  username = request.user.get_username() # Get login-user-information to store his name in the list for checking cliked status.

  if username in object.personsWhoRead: # Condition for clicked or unclicked.
    return redirect('snslistfunc')
  else:
    object.snsRead += 1
    object.personsWhoRead = object.personsWhoRead + " " + username
    object.save()
    return redirect('snslistfunc')



class BoardCreate(CreateView):
  template_name = 'board/snscreate.html'
  model = Board
  fields = ('snsTitle', 'snsContent', 'snsAuthor', 'snsImage')
  success_url = reverse_lazy('snslistfunc')
