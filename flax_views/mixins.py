from django.core.exceptions import ImproperlyConfigured


class PageTitleMixin(object):
    title = None

    def get_context_data(self, **kwargs):
        c = super(PageTitleMixin, self).get_context_data(**kwargs)
        if self.title is None:
            raise ImproperlyConfigured(
                '%(view)s title variable is not set.' % dict(view=self.__class__.__name__))
        c['title'] = self.title.capitalize()
        return c