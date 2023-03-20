# from django.shortcuts import render
from django.views import generic
from .models import JournalPost



# class IndexView(generic.TemplateView):
#   template_name = 'journal/post_list.html'
class IndexView(generic.ListView):
  model = JournalPost

  def get_queryset(self):
    return JournalPost.objects.order_by('-created_date')
