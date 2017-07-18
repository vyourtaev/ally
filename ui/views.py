# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from ui.models import Application
import docker

client = docker.from_env()


def index(request, format=None):
    apps = Application.objects.all().order_by('group', 'name')
    return render(request, 'index.html', {'apps':  apps})


def services(request, format=None):
    services = client.services.list()
    return render(request, 'service.html', {'services': services})


def nodes(request, format=None):
    nodes = client.nodes.list()
    return render(request, 'nodes.html', {'nodes': nodes})


def images(request, format=None):
    images = client.images.list()
    return render(request, 'images.html', {'images': images})
