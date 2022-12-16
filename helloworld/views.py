from django.shortcuts import render
from django.http import HttpResponse



def helloworldfunction(request):
  returnedobject = HttpResponse('<h1>HELLO WORLD</h1>')
  return returnedobject