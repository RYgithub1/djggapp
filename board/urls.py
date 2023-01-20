from django.urls import path
from . import views



urlpatterns = [
    path('signup/', views.signupfunc, name='signupfunc'),
    path('login/', views.loginfunc, name='loginfunc'),
    path('snslist/', views.snslistfunc, name='snslistfunc'),
    path('logout/', views.logoutfunc, name='logoutfunc'),
    path('snsdetail/<int:pk>/', views.snsdetailfunc, name='snsdetailfunc'),
    path('likeit/<int:pk>/', views.likeitfunc, name='likeitfunc'),
    path('readit/<int:pk>/', views.readitfunc, name='readitfunc'),
    path('create/', views.BoardCreate.as_view(), name='createfunc'),
]