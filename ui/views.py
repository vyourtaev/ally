# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from ui.models import Application
import docker

client = docker.from_env()


def index(request, format=None):
    apps = Application.objects.all().order_by('group', 'name')
    return render(request, 'index.html', {'apps':  apps})


class PaginationBaseView(TemplateView):
    default_view = None

    def get_context_data(self, **kwargs):
        context = super(PaginationBaseView, self).get_context_data(**kwargs)
        items = getattr(client, self.default_view).list()

        paginator = Paginator(items, 5)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        context[self.default_view] = show_lines
        return context


class ImagesView(TemplateView):
    template_name = 'images.html'

    def get_context_data(self, **kwargs):
        context = super(ImagesView, self).get_context_data(**kwargs)
        images = client.images.list()

        paginator = Paginator(images, 10)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        context['images'] = show_lines
        return context


class NodesView(TemplateView):
    template_name = 'nodes.html'

    def get_context_data(self, **kwargs):
        context = super(NodesView, self).get_context_data(**kwargs)
        nodes = client.nodes.list()

        paginator = Paginator(nodes, 10)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        context['nodes'] = show_lines
        return context
