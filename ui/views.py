# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from api.models import Service


def index(request, format=None):
    services = Service.objects.all()
    return render(request, 'index.html', {'services':  services})
