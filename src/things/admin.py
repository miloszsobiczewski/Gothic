from django.utils import timezone

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Thing, Warranty


@admin.register(Thing)
class PlanAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ["thing", "date", "comment", "checks", "bought"]

    def checks(self, obj):
        if not obj.approved:
            if obj.date and obj.date < timezone.now().date():
                obj.approved = True
                obj.save(update_fields=["approved"])
        color = {True: "green", False: "red"}
        html = '<button class="button" style="background-color:%s">%s</button>' % (
            color[obj.approved],
            obj.approved,
        )

        return mark_safe(html)


@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    model = Warranty
    list_display = ["thing", "start_date", "end_date", "receipt", "is_active"]

    def is_active(self, obj):
        return (
            mark_safe(
                f"<button class='button' style='background-color:green'>True</button>"
            )
            if obj.end_date < timezone.now().date()
            else mark_safe(
                f"<button class='button' style='background-color:red'>False</button>"
            )
        )
