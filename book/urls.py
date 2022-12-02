from django.urls import path
from . import views



urlpatterns = [
    path('', views.firstviewfunction, name='firstviewfunction'),
    path('download/<int:pk>/', views.downloadview, name='download'),
    path('detail/<int:pk>/', views.detailview, name='detail'),
    path('page/', views.indexview, name='index'),
]
