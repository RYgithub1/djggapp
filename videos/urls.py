from django.urls import path
from . import views



urlpatterns = [
    path('', views.VideoIndexView.as_view(), name='videoindexview'),
    path('upload/', views.VideoCreateView.as_view(), name='videocreateview'),
    path('play/<int:pk>/', views.VideoPlayView.as_view(), name='videoplayview'),
]