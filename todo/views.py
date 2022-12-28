from .models import TodoModel
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

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


class TodoCreate(CreateView):
  template_name = 'todo/create.html'
  model = TodoModel
  fields = ('title', 'memo', 'priority', 'duedate')

  ## NEED: Transfer to an URL(name=TodoList) after CREATE.
  ## After SAVE, transfer slowly(lazily).
  success_url = reverse_lazy('TodoList')