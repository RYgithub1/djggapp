from django.urls import path
from . import views



urlpatterns = [
    path('', views.videoslist, name='videoslist'),
]