from django.urls import path
from . import views



urlpatterns = [
    path('', views.TodoList.as_view(), name='TodoList'), # CLASS -> as_view()
    path('detail/<int:pk>/', views.TodoDetail.as_view(), name='TodoDetail'),
    path('create', views.TodoCreate.as_view(), name='TodoCreate'),
]
