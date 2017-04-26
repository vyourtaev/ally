# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170418_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('created_t', models.DateTimeField(auto_now_add=True, verbose_name='Deployed')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variables', to='api.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('volume', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('created_t', models.DateTimeField(auto_now_add=True, verbose_name='Deployed')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volumes', to='api.Service')),
            ],
        ),
    ]