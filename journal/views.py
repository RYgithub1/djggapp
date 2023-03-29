from django.shortcuts import get_object_or_404
from django.views import generic
from .models import JournalPost, JournalCategory
from django.db.models import Q



# class IndexView(generic.TemplateView):
#   template_name = 'journal/post_list.html'
class IndexView(generic.ListView):
  model = JournalPost
  paginate_by = 4

  def get_queryset(self):
    queryset = JournalPost.objects.order_by('-created_date')

    keyword = self.request.GET.get('search_keyword_1')
    if keyword:
      ## SINGLE
      # queryset = queryset.filter(title=keyword) ## Exact match
      # queryset = queryset.filter(title__contains=keyword) ## Partial match: lowercase-uppercase
      # queryset = queryset.filter(title__icontains=keyword) ## Partial match: both case
      ## MULTI
      queryset = queryset.filter(
        Q(title__icontains=keyword) | Q(text__icontains=keyword)
      )

    return queryset



class CategoryView(generic.ListView):
  model = JournalPost # JournalCategory:X
  paginate_by = 6

  def get_queryset(self):
    a_category = get_object_or_404(JournalCategory, pk=self.kwargs['pk'])
    queryset = JournalPost.objects.order_by('-created_date').filter(category=a_category)
    return queryset
