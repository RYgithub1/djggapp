from .models import TodoModel
from django.views.generic import ListView, DetailView

'''
TODO:
FIXME:
HACK:
'''

class TodoList(ListView):
  template_name = 'todo/list.html'
  model = TodoModel



class TodoDetail(DetailView):
  template_name = 'todo/detail.html'
  model = TodoModel