from django.urls import path
from . import views



urlpatterns = [
    path('', views.firstviewfunction, name='firstviewfunction'),
    path('download/<int:pk>/', views.downloadview, name='download'),
    path('detail/<int:pk>/', views.detailview, name='detail'),
    path('page/', views.indexview, name='index'),

    # path('redirect1/<int:pk>/', views.redirectview, name='redirectview'),
    path('redirect/<int:pk>/', views.redirectview, name='redirectview'),

    path('redirected/', views.listview, name='list'),
    path('listredirect/', views.redirectview1, name='redirectview1'),
]
