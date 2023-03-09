from django.urls import path
from . import views



urlpatterns = [
    path('', views.EmployIndexView.as_view(), name='EmployIndexView'),
]
