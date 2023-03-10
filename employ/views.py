from django.views.generic import TemplateView, ListView
from .models import Employ



# class EmployIndexView(generic.TemplateView):
#  template_name = 'employ/employ_list.html'
class EmployIndexView(ListView):
  model = Employ
