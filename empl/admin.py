from django.contrib import admin

from empl.models import Empl


@admin.register(Empl)
class EmplAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "post")
