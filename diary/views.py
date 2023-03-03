from django.shortcuts import render, redirect
from .forms import DayCreateForm
from .models import Day



def diary_index(request):
  day_list = Day.objects.all()
  content = {
    'day_list':day_list,
  }
  return render(request, 'diary/day_list.html', content)



def diary_add(request):
  form = DayCreateForm(request.POST or None)  # if no POST -> None

  if request.method == 'POST' and form.is_valid():
    form.save()
    # POST -> redirect stop duprication
    return redirect('diary_index')

  context = {
    'form': form
  }
  return render(request, 'diary/day_form.html', context)

