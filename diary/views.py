from django.shortcuts import render
from .forms import DayCreateForm



def diary_index(request):
  content = {}
  return render(request, 'diary/day_list.html', content)



def diary_add(request):
  context = {
    'form': DayCreateForm()
  }
  return render(request, 'diary/day_form.html', context)

