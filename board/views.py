from django.http import HttpResponse
from django.shortcuts import render




def qwerty(request):
  return HttpResponse('RESPONSED')


def signupfunc(request):
  return render(request, 'signup.html', {})