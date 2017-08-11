from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'suggestion/create$', views.SuggestionCreateView.as_view(), name='suggestion_create'),
    url(r'image/add', views.ImageCreateView.as_view(), name='image_create'),
    url(r'gallery', views.ImageListView.as_view(), name='image_list'),
]