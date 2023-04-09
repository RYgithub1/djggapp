from django.urls import reverse_lazy
from django.views import generic
# from .forms import VideoCreateForm
from .models import Video



class VideoIndexView(generic.ListView):
  model = Video



class VideoCreateView(generic.CreateView):
  model = Video
  # form_class = VideoCreateForm
  success_url = reverse_lazy('videoindexview')



class VideoPlayView(generic.DetailView):
  model = Video
