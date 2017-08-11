from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Suggestion(models.Model):
    username = models.CharField(max_length=155, unique=True, )
    your_suggestion = models.TextField(null=False, blank=False, help_text='brief info.')
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.username


class Image(models.Model):
    pic = models.ImageField(verbose_name='Image', blank=True, null=True)
    caption = models.CharField(max_length=155)