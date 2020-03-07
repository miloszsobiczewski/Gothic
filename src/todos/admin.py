from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Plan, Film, Book


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


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    model = Film
    list_display = [
        "title",
        "author",
        "score",
        "comment",
        "date_added",
        "status_button",
    ]

    def status_button(self, obj):
        color = {
            "todo": "gray",
            "in_progress": "orange",
            "done": "green",
        }
        html = '<button class="button" style="background-color:%s">%s</button>' % (
            color[obj.status],
            obj.status,
        )
        return mark_safe(html)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = [
        "title",
        "author",
        "score",
        "comment",
        "date_added",
        "status_button",
    ]

    def status_button(self, obj):
        color = {
            "todo": "gray",
            "in_progress": "orange",
            "done": "green",
        }
        html = '<button class="button" style="background-color:%s">%s</button>' % (
            color[obj.status],
            obj.status,
        )
        return mark_safe(html)
