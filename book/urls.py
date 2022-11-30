from django.urls import path
from . import views



urlpatterns = [
    path('', views.firstviewfunction, name='firstviewfunction'),
    path('/download/<int:pk>', views.downloadview, name='download'),
]
