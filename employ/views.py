from django.views.generic import TemplateView, ListView
from .models import Employ
from .forms import SearchForm



# class EmployIndexView(generic.TemplateView):
#  template_name = 'employ/employ_list.html'
class EmployIndexView(ListView):
  model = Employ


  def get_context_data(self):
    context = super().get_context_data()
    context['form'] = SearchForm(self.request.GET)
    return context


  def get_queryset(self):
    form = SearchForm(self.request.GET)
    form.is_valid()
    queryset = super().get_queryset()

    department_yade = form.cleaned_data['department']
    if department_yade:
        queryset = queryset.filter(department=department_yade)

    club_yade = form.cleaned_data['club']
    if club_yade:
        queryset = queryset.filter(club=club_yade)

    return queryset
