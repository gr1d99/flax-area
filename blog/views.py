from django.shortcuts import render
from django.views.generic import TemplateView
from engagement.forms import ImageForm, SuggestionForm
from engagement.models import Suggestion

from flax_views.mixins import PageTitleMixin


class FlaxIndexView(PageTitleMixin, TemplateView):
    template_name = 'blog/index.html'
    title = 'index'

    def get_context_data(self, **kwargs):
        c = super(FlaxIndexView, self).get_context_data(**kwargs)
        c['suggestion_form'] = SuggestionForm()
        c['image_form'] = ImageForm()
        suggestions = Suggestion.objects.all()
        c['suggestions'] = suggestions
        return c