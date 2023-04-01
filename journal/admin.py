from django.contrib import admin
from .models import JournalCategory, JournalPost, JournalComment



admin.site.register(JournalCategory)
admin.site.register(JournalPost)
admin.site.register(JournalComment)
