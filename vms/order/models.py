from django.db import models

from order.choices import PO_STATUS_CHOICES
from vendor.models import Vendor


# Create your models here.
class Order(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        blank=True,
        related_name="Vendors",
    )
    po_number = models.CharField(max_length=255, unique=True)
    order_date = models.DateTimeField(help_text="Date when the order was placed")
    delivery_date = models.DateTimeField(
        help_text=" Expected or actual delivery date of the order"
    )
    items = models.JSONField(help_text="Details of items ordered")
    quantity = models.IntegerField(help_text="Total quantity of items in the PO")
    status = models.CharField(
        max_length=50, help_text="Current status of the PO", choices=PO_STATUS_CHOICES
    )
    quality_rating = models.FloatField(
        null=True, blank=True, help_text="Rating given to the vendor for this PO"
    )
    issue_date = models.DateTimeField(
        help_text="Timestamp when the PO was issued to the vendor"
    )
    acknowledgment_date = models.DateTimeField(
        null=True, blank=True, help_text="Timestamp when the vendor acknowledged the PO"
    )
    po_delivered_on = models.DateTimeField(
        null=True, blank=True, help_text="actual time when the PO is sucessfully delivered"
    )

    def __str__(self):
        return self.po_number
