# views.py
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order
from performance_history.serializers import HistoricalPerformanceSerializer
from performance_history.utils import VendorPerformanceCalculator
from vendor.models import Vendor


class VendorPerformanceAPIView(APIView):
    """
    API endpoint to calculate and save performance metrics for a vendor.
    Returns:
        Response: A JSON response containing the calculated performance metrics and vendor information.
    """

    def get(self, request, vendor_id):
        """
        Calculate and save performance metrics for the specified vendor.
        """
        try:
            # Retrieve the vendor instance
            vendor = Vendor.objects.get(id=vendor_id)

            # Calculate performance metrics using VendorPerformanceCalculator
            performance_calculator = VendorPerformanceCalculator(vendor_id)
            performance_data = performance_calculator.calculate_performance_metrics()

            #Update the vendor profile performance matrix data
            vendor.on_time_delivery_rate = performance_data['on_time_delivery_rate']
            vendor.quality_rating_avg = performance_data['quality_rating_avg']
            vendor.fulfillment_rate = performance_data['fulfillment_rate']
            vendor.save()

            performance_metrics = {"vendor": vendor_id, "created_at": timezone.now()}
            performance_metrics.update(performance_data)

            serializers = HistoricalPerformanceSerializer(data=performance_metrics)

            if serializers.is_valid():
                serializers.save()

            # Construct response data
            response_data = {
                "vendor_code": vendor.vendor_code,
                **performance_data,
            }
            return Response(response_data)
        except Vendor.DoesNotExist:
            return Response(
                {"message": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UpdateAcknowledgmentEndpoint(APIView):
    """
    API endpoint to update acknowledgment date for a purchase order.
    """

    def post(self, request, po_id):
        """
        Update acknowledgment date for the specified purchase order.
        Returns:
            Response: A JSON response indicating the success or failure of the acknowledgment update.
        """
        try:
            # Retrieve the purchase order
            purchase_order = Order.objects.get(po_number=po_id)

            # Update the acknowledgment date
            purchase_order.acknowledgment_date = timezone.now()
            purchase_order.save()

            # Trigger recalculation of average response time
            performance_calculator = VendorPerformanceCalculator(
                purchase_order.vendor_id
            )
            average_response_time = (
                performance_calculator.calculate_average_response_time()
            )
             

            # Update vendor's average response time
            vendor = Vendor.objects.get(id=purchase_order.vendor_id)
            vendor.average_response_time = round(average_response_time, 2)
            vendor.save()

            # Return success response
            return Response(
                {"message": "Purchase order acknowledged successfully"},
                status=status.HTTP_200_OK,
            )
        except Order.DoesNotExist:
            return Response(
                {"message": "Purchase order not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
