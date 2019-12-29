from django.contrib import admin
from .models import Jeep


@admin.register(Jeep)
class JeepAdmin(admin.ModelAdmin):
    model = Jeep
    ordering = ["-miledge"]
    list_display = [
        "miledge",
        "task",
        "date",
        "mechanic",
        "parts_price",
        "labor_price",
        "details",
        "done",
    ]
