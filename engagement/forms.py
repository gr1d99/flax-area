from django import forms
from django.forms.models import modelformset_factory
from .models import Image, Suggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        exclude = ('timestamp',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

    def save(self, commit=True):
        obj = super(ImageForm, self).save(commit=False)
        obj.save()
        return obj
