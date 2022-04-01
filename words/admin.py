from django.contrib import admin
from words.models import *
# Register your models here.
admin.site.register(Word)
admin.site.register(AudioStore)
admin.site.register(Score)
admin.site.register(CorrectWord)