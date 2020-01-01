from datetime import date

from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils import timezone

from .models import Thing


@admin.register(Thing)
class PlanAdmin(admin.ModelAdmin):
    model = Thing
    list_display = [
        "thing",
        "date",
        "comment",
        "checks",
    ]

    def checks(self, obj):
        if not obj.approved:
            if obj.date and obj.date < date.today():
                obj.approved = True
                obj.save(update_fields=["approved"])
        color = {True: "green", False: "red"}
        html = '<button class="button" style="background-color:%s">%s</button>' % (
            color[obj.approved],
            obj.approved,
        )

        return mark_safe(html)
