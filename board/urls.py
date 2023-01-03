from django.urls import path
from . import views



urlpatterns = [
    path('', views.qwerty, name='qwerty'),
    path('signup/', views.signupfunc, name='signupfunc'),
]