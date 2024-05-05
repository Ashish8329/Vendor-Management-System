from django.contrib import admin
from django.utils import timezone
from performance_history.models import HistoricalPerformance

# Register your models here.


@admin.register(HistoricalPerformance)
class UserAnalyticsHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    list_display = (
        "id",
        "vendor",
    )
    empty_value_display = "-None-"
    search_fields = ("vendor",)

    def save_model(self, request, obj, form, change):

        obj.created_at = timezone.now()
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.save()
