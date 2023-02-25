from django.urls import path
from . import views


urlpatterns = [
    path('', views.myapp_index, name='myapp_index'), # 127.0.0.1:8000/myapp
    path('about/', views.myapp_about, name='myapp_about'),
    path('info/', views.myapp_info, name='myapp_info'),
]
