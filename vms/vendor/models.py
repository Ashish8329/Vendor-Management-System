from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(
        max_length=50, unique=True, verbose_name="Vendor code"
    )
    on_time_delivery_rate = models.FloatField(
        null=True, help_text="On-time delivery rate"
    )
    quality_rating_avg = models.FloatField(
        null=True, help_text="Average quality rating based on purchase orders"
    )
    average_response_time = models.FloatField(
        null=True, help_text="Average response time to acknowledge purchase orders"
    )
    fulfillment_rate = models.FloatField(
        null=True, help_text="Fulfillment rate of purchase orders"
    )

    def __str__(self):
        return str(self.id)
