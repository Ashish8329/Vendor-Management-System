from django.contrib import admin
from django.utils import timezone
from order.models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = (
        "id",
        "vendor",
        "po_number",
        "status",
    )
    empty_value_display = "-None-"
    search_fields = ("vendor",)

    def save_model(self, request, obj, form, change):

        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.save()
