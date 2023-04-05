from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .forms import CommentCreateForm
from .models import JournalPost, JournalCategory, JournalComment
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



class DetailView(generic.DetailView):
  model = JournalPost  # HTMLNAME = modelname_viewname.py = journalpost_detail.py



class CommentView(generic.CreateView):
  model = JournalComment

  form_class = CommentCreateForm
  # fields = ('name', 'comment')

  def form_valid(self, form):
    post_pk = self.kwargs['post_pk']
    comment = form.save(commit=False)
    comment.post = get_object_or_404(JournalPost, pk=post_pk)
    comment.save()
    return redirect('journal_detail', pk=post_pk)
