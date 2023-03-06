from django.urls import path
from . import views


urlpatterns = [
    path('', views.diary_index, name='diary_index'), # 127.0.0.1:8000/diary
    path('add/', views.diary_add, name='diary_add'),
    path('update/<int:pk>', views.diary_update, name='diary_update'),
    path('delete/<int:pk>', views.diary_delete, name='diary_delete'),
    path('detail/<int:pk>', views.diary_detail, name='diary_detail'),
]