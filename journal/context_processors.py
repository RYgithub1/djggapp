from .models import JournalCategory



def common(request):
  category_list = JournalCategory.objects.all()  # Data into templates everytime

  context = {
    'category_list':category_list,
  }

  return context
