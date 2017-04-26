# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170425_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='replicas',
            field=models.IntegerField(blank=True, null=True, verbose_name='Replicas'),
        ),
        migrations.AlterField(
            model_name='service',
            name='stack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='api.Stack'),
        ),
    ]