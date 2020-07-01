from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Jeep, Shooting, Quote


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


@admin.register(Shooting)
class ShootingAdmin(admin.ModelAdmin):
    model = Shooting
    ordering = ["-date"]
    list_display = [
        "year",
        "category",
        "date",
        "place",
        "competition",
        "score",
        "confirmation",
        "done",
        "download",
    ]

    def download(self, obj):
        if obj.confirmation:
            return format_html(
                '<a class="button" href="{}">Download</a>&nbsp;',
                reverse("shooting:download", args=[obj.pk]),
            )
        else:
            return "No attachment"


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    list_display = ("text", "author", "note", "date")
