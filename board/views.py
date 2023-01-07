from django.shortcuts import render
from django.contrib.auth.models import User



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
    user = User.objects.create_user(username, '', password)
  else:
    print("request.method == 'GET'")

  return render(request, 'board/signup.html', {'some': 11100})
