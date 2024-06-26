# Generated by Django 5.0.4 on 2024-05-05 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vendor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("po_number", models.CharField(max_length=255, unique=True)),
                (
                    "order_date",
                    models.DateTimeField(help_text="Date when the order was placed"),
                ),
                (
                    "delivery_date",
                    models.DateTimeField(
                        help_text=" Expected or actual delivery date of the order"
                    ),
                ),
                ("items", models.JSONField(help_text="Details of items ordered")),
                (
                    "quantity",
                    models.IntegerField(help_text="Total quantity of items in the PO"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Completed", "Completed"),
                            ("Canceled", "Canceled"),
                        ],
                        help_text="Current status of the PO",
                        max_length=50,
                    ),
                ),
                (
                    "quality_rating",
                    models.FloatField(
                        blank=True,
                        help_text="Rating given to the vendor for this PO",
                        null=True,
                    ),
                ),
                (
                    "issue_date",
                    models.DateTimeField(
                        help_text="Timestamp when the PO was issued to the vendor"
                    ),
                ),
                (
                    "acknowledgment_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="Timestamp when the vendor acknowledged the PO",
                        null=True,
                    ),
                ),
                (
                    "po_delivered_on",
                    models.DateTimeField(
                        blank=True,
                        help_text="actual time when the PO is sucessfully delivered",
                        null=True,
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Vendors",
                        to="vendor.vendor",
                    ),
                ),
            ],
        ),
    ]
