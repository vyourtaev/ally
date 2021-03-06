# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('port_ext', models.IntegerField(unique=True, verbose_name='Published port')),
                ('port_int', models.IntegerField(verbose_name='Internal port')),
                ('created_t', models.DateTimeField(auto_now_add=True, verbose_name='Deployed')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('image_name', models.CharField(max_length=256)),
                ('created_t', models.DateTimeField(auto_now_add=True, verbose_name='Deployed')),
            ],
        ),
        migrations.RenameField(
            model_name='stack',
            old_name='deployed_t',
            new_name='created_t',
        ),
        migrations.AddField(
            model_name='stack',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='stack',
            name='slug',
            field=models.SlugField(default=django.utils.datetime_safe.datetime.now, max_length=64, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stack',
            name='name',
            field=models.CharField(help_text='A user provided name for the service. This name will be             inherited by the service containers and will be used in endpoint             URLs, environment variable names, etc.', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='stack',
            name='version',
            field=models.CharField(max_length=8),
        ),
        migrations.AddField(
            model_name='service',
            name='stack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='api.Stack'),
        ),
        migrations.AddField(
            model_name='port',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ports', to='api.Service'),
        ),
    ]
