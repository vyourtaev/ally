from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ui.views import ImagesView, NodesView, index
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^docker_nodes$', NodesView.as_view(), name='docker_nodes'),
    url(r'^docker_images$', ImagesView.as_view(), name='docker_images'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
