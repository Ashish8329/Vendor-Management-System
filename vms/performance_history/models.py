from django.db import models

from vendor.models import Vendor


# Create your models here.
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        blank=True,
        related_name="vendors",
    )
    created_at = models.DateTimeField(help_text="Date of the performance record")
    on_time_delivery_rate = models.FloatField(
        null=True,
        blank=True,
        help_text="Historical record of the on-time delivery rate.",
    )
    average_response_time = models.FloatField(
        null=True,
        blank=True,
        help_text="Historical record of the average response time.",
    )
    quality_rating_avg = models.FloatField(
        null=True,
        blank=True,
        help_text="Historical record of the quality rating average.",
    )
    fulfillment_rate = models.FloatField(
        null=True, blank=True, help_text="Historical record of the fulfilment rate."
    )

    def __str__(self):
        return self.created_at
