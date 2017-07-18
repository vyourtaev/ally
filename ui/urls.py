from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^images/$', views.images, name='images'),
    url(r'^nodes$', views.nodes, name='nodes'),
    url(r'^services$', views.services, name='services'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
