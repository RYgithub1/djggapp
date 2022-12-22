from .models import TodoModel
from django.views.generic import ListView



class TodoList(ListView):
  template_name = 'todo/list.html'
  model = TodoModel
