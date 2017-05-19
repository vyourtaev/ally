from django.db import models
from api.models import Service


class Application(models.Model):
    """
    Application
    """

    GROUP_CHOICES = (
        ('xms', 'xms'),
        ('sms', 'sms'),
        ('ws', 'ws'),
        ('farm', 'farm'),
        ('cube', 'active-pivot'),
        ('cube', 'active-pivot'),
        ('svc', 'service'),
        ('elk', 'elk'),
    )

    name = models.CharField(max_length=256)
    group = models.CharField(
        max_length=64,
        choices=GROUP_CHOICES,
        default=('svc'),
        blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE,
        related_name='application',
        blank=True, null=True)
    version = models.CharField(max_length=64, blank=True, null=True)
    created_t = models.DateTimeField('Created', auto_now_add=True)
    tag = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name


class ApplicationURL(models.Model):
    """
    Application URLs
    """

    url = models.URLField(max_length=256)
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    application = models.ForeignKey(
        Application, on_delete=models.CASCADE,
        related_name='urls')
    created_t = models.DateTimeField('Created', auto_now_add=True)

    def __str__(self):
        return self.url
