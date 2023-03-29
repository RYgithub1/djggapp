from django.urls import path
from . import views


''

urlpatterns = [
    path('', views.IndexView.as_view(), name='journal_index'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='journal_category'),
]
