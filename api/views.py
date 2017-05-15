# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from api.models import Stack, Service
from api.serializers import StackSerializer, ServiceSerializer
from rest_framework.views import APIView

# from api.forms import ServiceUploadForm


def index(request, format=None):
    service = Service.objects.get(pk=3)
    return render(request, 'service.html', { 'service':  service })

class StackList(generics.ListCreateAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer


class StackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

def ImportService(request):
    form = ServiceUploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    else:
        pass
        # display errors
