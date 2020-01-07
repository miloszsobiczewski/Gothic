from django.contrib import admin
from django.db.models import Count, Sum, Min, Max, DateTimeField
from django.db.models.functions import Trunc

from .models import TimeTracker, TimeSummary


def make_paid(modeladmin, request, queryset):
    queryset.update(paid=True)


@admin.register(TimeTracker)
class SadAdmin(admin.ModelAdmin):
    model = TimeTracker
    ordering = ["-timestamp"]
    list_display = [
        "workday",
        "task",
        "description",
        "time_effort",
        "timestamp",
        "paid",
    ]
    actions = [make_paid]


@admin.register(TimeSummary)
class SaleSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/time_summary_change_list.html"
    date_hierarchy = "workday"
    list_filter = ("task",)

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data["cl"].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {"count": Count("uuid"), "total_time": Sum("time_effort")}
        response.context_data["summary"] = list(
            qs.values("task").annotate(**metrics).order_by("-total_time")
        )
        response.context_data["summary_total"] = dict(qs.aggregate(**metrics))
        return response
