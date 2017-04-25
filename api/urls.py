from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stacks/$', views.StackList.as_view()),
    url(r'^stacks/(?P<pk>[0-9]+)/$', views.StackDetail.as_view()),
    url(r'^services/$', views.ServiceList.as_view()),
    url(r'^services/(?P<pk>[0-9]+)/$', views.ServiceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
