# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedTabularInline, \
                                NestedModelAdmin
from api.models import Stack, Service, Port, Variable, Volume
from api.forms import StackForm, ServiceForm, VariableForm, VolumeForm


class PortInline(NestedStackedInline):
    fields = (('port_ext', 'port_int'), ('name', 'description'))
    model = Port
    extra = 0
    fk_name = 'service'


class VariableInline(NestedStackedInline):
    fields = (('name', 'value'), 'description')
    model = Variable
    extra = 0
    fk_name = 'service'
    form = VariableForm


class VolumeInline(NestedStackedInline):
    fields = (('name', 'volume'), 'description')
    model = Volume
    extra = 0
    fk_name = 'service'
    form = VolumeForm


class ServiceInline(NestedStackedInline):
    fields = (('name', 'description'), 'image_name')
    model = Service
    extra = 1
    fk_name = 'stack'
    form = ServiceForm
    inlines = [PortInline, VariableInline, VolumeInline]
    list_display = ('name', 'created_t', 'status')


@admin.register(Stack)
class StackAdmin(NestedModelAdmin):
    model = Stack
    inlines = [ServiceInline]
    prepopulated_fields = {"slug": ("name",)}
    form = StackForm
    list_display = ('name', 'created_t')
    view_on_site = True

def make_atatus_off(modeladmin, request, queryset):
    queryset.update(status='False')
make_atatus_off.nshort_description = "Activate selected services"

def make_atatus_on(modeladmin, request, queryset):
    queryset.update(status='True')
make_atatus_on.nshort_description = "Deactivate selected services"

@admin.register(Service)
class ServiceAdmin(NestedModelAdmin):
    model = Service
    list_display = ('name', 'created_t', 'status')
    actions = [make_atatus_on, make_atatus_off]
    inlines = [PortInline, VariableInline, VolumeInline]
