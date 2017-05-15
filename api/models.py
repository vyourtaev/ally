# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Environment(models.Model):
    """
    Environment general
    """
    ENV_CHOICES = (
        ('DEV', 'DEV'),
        ('INT', 'INT'),
        ('PPE', 'PPE'),
    )
    name = models.CharField(
        max_length=64,
        choices=ENV_CHOICES,
        default=('DEV'),
        unique=True
    )
    description = models.CharField(max_length=128, blank=True, null=True)
    created_t = models.DateTimeField('Created', auto_now_add=True)

    def __str__(self):
        return self.name



class Stack(models.Model):
    """Docker Stack mode"""
    VERSION_CHOICES = (
        ('3.0', '3.0'),
        ('3.1', '3.1'),
        ('3.2', '3.2')
    )
    version = models.CharField(
        max_length=8, choices=VERSION_CHOICES, default="3.0")
    name = models.CharField(
        max_length=64,
        unique=True,
        help_text="A user provided name for the service. This name will be \
            inherited by the service containers and will be used in endpoint \
            URLs, environment variable names, etc.")
    description = models.CharField(max_length=256, blank=True, null=True)
    slug = models.SlugField(max_length=64, unique=True)
    created_t = models.DateTimeField('Created', auto_now_add=True)
    environment = models.ForeignKey(
        Environment, on_delete=models.CASCADE,
        related_name='stacks',
        null=True, blank=True)

    class Meta:
        verbose_name_plural = "Stacks"
        ordering = ('created_t',)

    def get_absolute_url(self):
            return "/api/stacks/%i/" % self.id

    def __str__(self):
        return "{0}".format(self.name)


class Service(models.Model):
    """Docker Service Model"""

    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256, blank=True, null=True)
    image_name = models.CharField('Image', max_length=256)
    image_version = models.CharField('v.', max_length=64, default='latest')
    replicas = models.IntegerField('Replicas', default=1, blank=True, null=True)
    stack = models.ForeignKey(
        Stack, on_delete=models.CASCADE,
        related_name='services',
        null=True, blank=True)
    environment = models.ForeignKey(
        Environment, on_delete=models.CASCADE,
        related_name='services',
        null=True, blank=True)

    status = models.BooleanField(
        'Status',
        default="False",
        help_text="Is active")
    created_t = models.DateTimeField('Deployed', auto_now_add=True)

    class Meta:
        verbose_name_plural = "Services"

    def get_absolute_url(self):
            return "/api/services/%i/" % self.id

    def __str__(self):
        return self.name


class Port(models.Model):
    """Published ports for service"""

    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256, blank=True, null=True)
    port_ext = models.IntegerField('Published port', unique=True)
    port_int = models.IntegerField('Internal port')
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                related_name='ports')
    created_t = models.DateTimeField('Deployed', auto_now_add=True)

    class Meta:
        verbose_name_plural = "Ports"

    def __str__(self):
        return '%d: %s' % (self.port_ext, self.port_int)


class Variable(models.Model):
    """Array of Environment variables"""

    name = models.CharField(max_length=256)
    value = models.CharField(max_length=256)
    description = models.CharField(max_length=256, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                related_name='variables')
    created_t = models.DateTimeField('Deployed', auto_now_add=True)

    def __str__(self):
        return self.name


class Volume(models.Model):
    """Array of Volumes for service"""

    name = models.CharField(max_length=256)
    volume = models.CharField(max_length=256)
    description = models.CharField(max_length=256, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                related_name='volumes')
    created_t = models.DateTimeField('Deployed', auto_now_add=True)

    def __str__(self):
        return self.name




