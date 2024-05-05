from django.contrib import admin
from django.utils import timezone
from vendor.models import Vendor

# Register your models here.


@admin.register(Vendor)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        "on_time_delivery_rate",
        "quality_rating_avg",
        "average_response_time",
        "fulfillment_rate",
    )
    list_display = (
        "id",
        "vendor_code",
    )
    empty_value_display = "-None-"
    search_fields = ("vendor_code",)

    def save_model(self, request, obj, form, change):

        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.save()
