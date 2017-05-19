# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from ui.models import Application


def index(request, format=None):
    apps = Application.objects.all()
    return render(request, 'index.html', {'apps':  apps})
