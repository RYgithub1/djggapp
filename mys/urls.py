"""mys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('adminadmin/', admin.site.urls),

    ## BLOG APP
    path('', include('blog.urls')),
    ## BOOK APP
    path('book/', include('book.urls')),
    ## HELLOWORLD APP
    path('helloworld/', include('helloworld.urls')),
    ## TODo APP
    path('todo/', include('todo.urls')),
    ## BOARD APP
    path('board/', include('board.urls')),
    ## MYAPP APP
    path('myapp/', include('myapp.urls')),
    ## DIARY APP
    path('diary/', include('diary.urls')),
    ## EMPLOY APP
    path('employ/', include('employ.urls')),
    ## JOURNAL APP
    path('journal/', include('journal.urls')),
    ## VIDEOS APP
    path('videos/', include('videos.urls')),
    ## MNIST APP
    path('mnist/', include('mnist.urls')),
    ## NEWS APP
    path('news/', include('news.urls')),
    ## POLLS APP
    path('polls/', include('polls.urls')),

    ## Model data to a multiple html pages with urls/template without views function. Ex: Pages of Privacy/Contact/Invenstment.
    path('flatpage/', include('django.contrib.flatpages.urls')),
    ## Envoke urls of flatpages.
    ### (1)BASE_URL/flatpage/privacy/
    ### (2)BASE_URL/flatpage/sustainability/
]

if settings.DEBUG:
    # Likewise path, tell the url for rooting, and storage the date in the media directory.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)