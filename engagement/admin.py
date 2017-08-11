from django.contrib import admin

from .models import Image, Suggestion

admin.site.register(Suggestion)
admin.site.register(Image)