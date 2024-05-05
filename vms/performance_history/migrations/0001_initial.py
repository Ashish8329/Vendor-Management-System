# Generated by Django 5.0.4 on 2024-05-04 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vendor", "0006_alter_vendor_average_response_time_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalPerformance",
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
                (
                    "created_at",
                    models.DateTimeField(help_text="Date of the performance record"),
                ),
                (
                    "on_time_delivery_rate",
                    models.FloatField(
                        blank=True,
                        help_text="Historical record of the on-time delivery rate.",
                        null=True,
                    ),
                ),
                (
                    "average_response_time",
                    models.FloatField(
                        blank=True,
                        help_text="Historical record of the average response time.",
                        null=True,
                    ),
                ),
                (
                    "quality_rating_avg",
                    models.FloatField(
                        blank=True,
                        help_text="Historical record of the quality rating average.",
                        null=True,
                    ),
                ),
                (
                    "fulfillment_rate",
                    models.FloatField(
                        blank=True,
                        help_text="Historical record of the fulfilment rate.",
                        null=True,
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vendors",
                        to="vendor.vendor",
                    ),
                ),
            ],
        ),
    ]