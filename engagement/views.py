import mimetypes

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import ImageForm, SuggestionForm
from .models import Image

from flax_views.mixins import PageTitleMixin


class SuggestionCreateView(PageTitleMixin, CreateView):
    form_class = SuggestionForm
    title = 'Create Suggestion'
    template_name = 'blog/index.html'
    suggestion_form_error = False

    def get_success_url(self):
        messages.success(self.request, 'Thank you for your suggestion, we will review it and if it is viable we will'
                                       ' consider. Kindly click on the Whatsapp share button below so that we can gather as much'
                                       ' as possible information.')
        return reverse('blog:index')

    def form_invalid(self, form):
        self.suggestion_form_error = True
        return super(SuggestionCreateView, self).form_invalid(form)


    def get_context_data(self, **kwargs):
        c = super(SuggestionCreateView, self).get_context_data(**kwargs)
        c['suggestion_form_error'] = self.suggestion_form_error
        return c


class ImageCreateView(PageTitleMixin, CreateView):
    title = 'Gallery'
    form_class = ImageForm
    model = Image
    template_name = 'blog/index.html'
    image_form_error = False

    def form_valid(self, form):
        return super(ImageCreateView, self).form_valid(form)

    def form_invalid(self, form):
        self.image_form_error = True
        return super(ImageCreateView, self).form_invalid(form)


    def get_success_url(self):
        return reverse('engagement:image_list')

    def get_context_data(self, **kwargs):
        c = super(ImageCreateView, self).get_context_data(**kwargs)
        c['image_form_error'] = self.image_form_error
        return c


class ImageListView(PageTitleMixin, ListView):
    title = 'Gallery'
    model = Image
    template_name = 'blog/gallery/images.html'

