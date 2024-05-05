# Generated by Django 5.0.3 on 2024-05-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendor", "0007_alter_vendor_fulfillment_rate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="average_response_time",
            field=models.FloatField(
                help_text="Average response time to acknowledge purchase orders in (hr:mm)",
                null=True,
            ),
        ),
    ]
