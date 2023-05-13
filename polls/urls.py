from django.urls import path
from . import views



urlpatterns = [
    path("", views.pollsindex, name="pollsindex"),
    path("<int:question_id>/", views.pollsdetail, name="pollsdetail"),
    path("<int:question_id>/results/", views.pollsresults, name="pollsresults"),
    path("<int:question_id>/vote/", views.pollsvote, name="pollsvote"),
]
