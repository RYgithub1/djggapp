from django.urls import path
from . import views


''

urlpatterns = [
    path('', views.IndexView.as_view(), name='journal_index'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='journal_category'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='journal_detail'),
    path('comment/<int:post_pk>/', views.CommentView.as_view(), name='journal_comment'),
]
