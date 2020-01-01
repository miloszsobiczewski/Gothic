from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    model = Plan
    list_display = [
        "group",
        "status_button",
        "task",
        "deadline",
        "comment",
    ]
    search_fields = ["group", "task"]

    def status_button(self, obj):
        color = {
            "todo": "gray",
            "in_progress": "yellow",
            "done": "green",
            "plan": "red",
            "hold": "blue",
        }
        html = '<button class="button" style="background-color:%s">%s</button>' % (
            color[obj.status],
            obj.status,
        )
        return mark_safe(html)
