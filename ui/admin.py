from django.contrib import admin
from ui.models import Application, ApplicationURL


class ApplicationURLInline(admin.TabularInline):
    model = ApplicationURL
    extra = 0


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    inlines = [ApplicationURLInline]
    save_as = True
