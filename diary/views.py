from django.shortcuts import render, redirect, get_object_or_404
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
    'form':form
  }
  return render(request, 'diary/day_form.html', context)



def diary_update(request, pk):
  day = get_object_or_404(Day, pk=pk)
  form = DayCreateForm(request.POST or None, instance=day)

  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect(diary_index)

  context = {
    'form':form,
  }
  return render(request, 'diary/day_form.html', context)



def diary_delete(request, pk):
  day = get_object_or_404(Day, pk=pk)

  if request.method == 'POST':
    day.delete()
    return redirect(diary_index)

  context = {
    'day':day,
  }
  return render(request, 'diary/day_confirm_delete.html', context)



def diary_detail(request, pk):
  day = get_object_or_404(Day, pk=pk)
  context = {
    'day':day,
  }
  return render(request, 'diary/day_detail.html', context)

