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
        help_text="Historical record of the  Percentage of orders delivered by the promised date",
    )
    average_response_time = models.FloatField(
        null=True,
        blank=True,
        help_text="Historical record of the average response time in (hr:mm).",
    )
    quality_rating_avg = models.FloatField(
        null=True,
        blank=True,
        help_text="Historical record of the quality rating average.",
    )
    fulfillment_rate = models.FloatField(
        null=True, blank=True, help_text="Historical record of Percentage of purchase orders fulfilled without issues."
    )
