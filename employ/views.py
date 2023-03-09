from django.views.generic import TemplateView



# class EmployIndexView(generic.TemplateView):
class EmployIndexView(TemplateView):
  template_name = 'employ/employ_list.html'
