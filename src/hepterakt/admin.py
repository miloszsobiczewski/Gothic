import datetime

from django.contrib import admin
from django.db.models import Count, Sum
from django.utils.safestring import mark_safe

from .models import TimeTracker, TimeSummary, Work


def make_paid(modeladmin, request, queryset):
    queryset.update(paid=True)


def make_last_month_paid(modeladmin, request, queryset):
    last_month = datetime.date.today().month - 1
    TimeTracker.objects.filter(workday__month=last_month).update(paid=True)


@admin.register(TimeTracker)
class TimeTrackerAdmin(admin.ModelAdmin):
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
    actions = [make_paid, make_last_month_paid]


@admin.register(TimeSummary)
class TimeSummaryAdmin(admin.ModelAdmin):
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


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    model = Work
    list_display = [
        "company",
        "contact_ind",
        "position",
        "money",
        "link",
        "application_date",
        "contact_date",
        "status",
        "applied_ind",
    ]

    def link(self, obj):
        return mark_safe(f"<a href={obj.url}>{obj.url}</a>")

    link.allow_tags = True
