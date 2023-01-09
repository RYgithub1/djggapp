from django.urls import path
from . import views



urlpatterns = [
    path('signup/', views.signupfunc, name='signupfunc'),
    path('login/', views.loginfunc, name='loginfunc'),
]