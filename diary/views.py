from django.shortcuts import render



def diary_index(request):
  content = {}
  return render(request, 'diary/day_list.html', content)
