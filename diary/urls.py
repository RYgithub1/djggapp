from django.urls import path
from . import views


urlpatterns = [
    path('', views.diary_index, name='diary_index'), # 127.0.0.1:8000/diary
]
