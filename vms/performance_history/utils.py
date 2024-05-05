from datetime import datetime, timedelta

from django.db.models import Avg, Count, F
from rest_framework import status

from order.models import Order

 

class VendorPerformanceCalculator:
    """
    A class to calculate performance metrics for a vendor.
    Args:
        vendor_id (int): The ID of the vendor.
    Methods:
        calculate_performance_metrics: Calculates various performance metrics such as on-time delivery rate,
        quality rating average, average response time, and fulfillment rate.
        calculate_average_response_time: Calculates the average response time for completed purchase orders.
        _calculate_on_time_delivery_rate: Calculates the on-time delivery rate.
    """

    def __init__(self, vendor_id):
        self.vendor_id = vendor_id

    def calculate_performance_metrics(self):
        """
        Calculates various performance metrics for the vendor.
        """
        try:
            #calculated total complted pos which are completed
            completed_pos = Order.objects.filter(
                vendor__id=self.vendor_id, status="Completed"
            )
            all_pos = Order.objects.filter(vendor__id=self.vendor_id)

            on_time_delivered_pos = completed_pos.filter(
                delivery_date__gte=F("acknowledgment_date")
            )
            successful_pos_count = all_pos.filter(
                status="Completed", quality_rating__isnull=False
            ).count()

            total_quality_rating = (
                completed_pos.filter(quality_rating__isnull=False).aggregate(
                    avg_quality_rating=Avg("quality_rating")
                )["avg_quality_rating"]
                or 0
            )

            average_response_time_hours = self.calculate_average_response_time()

            fulfillment_rate = (
                successful_pos_count / all_pos.count() if all_pos.count() != 0 else 0
            )

            return {
                "on_time_delivery_rate": self._calculate_on_time_delivery_rate(
                    on_time_delivered_pos, completed_pos.count()
                ),
                "quality_rating_avg": total_quality_rating,
                "average_response_time": round(average_response_time_hours, 2),
                "fulfillment_rate": fulfillment_rate,
            }
        except Exception as e:
            return None


    def calculate_average_response_time(self):
        """
        Calculates the average response time for completed purchase orders.
        Returns:
            float: The average response time in hours.
        """
        try:
            completed_pos = Order.objects.filter(
                vendor__id=self.vendor_id, status="Completed"
            )
            total_response_time = timedelta(seconds=0)
            total_completed_pos = completed_pos.count()

            for po in completed_pos.filter(acknowledgment_date__isnull=False):
                total_response_time += po.acknowledgment_date - po.issue_date

            return (
                total_response_time.total_seconds() / 3600 / total_completed_pos
                if total_completed_pos != 0
                else 0
            )
        except Exception as e:
            return None

    def _calculate_on_time_delivery_rate(
        self, on_time_delivered_pos, total_completed_pos
    ):
        """
        Calculates the on-time delivery rate.
        Returns:
            float: The on-time delivery rate.
        """
        return (
            on_time_delivered_pos.count() / total_completed_pos
            if total_completed_pos != 0
            else 0
        )
