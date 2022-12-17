from django.urls import path
from . import views



urlpatterns = [
    path('', views.helloworldfunction, name='helloworldfunction'),

    ## RULE: as_view(): Change CLASS to METHOD(/FUNCTION)
    path('helloworld2/', views.HelloWorldClass.as_view(), name='HelloWorldClass'),
    path('helloworldapp/', views.helloworldappview, name='helloworldappview'),
]