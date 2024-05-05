from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone

from order.models import Order
from order.serializers import PurchaseOrderSerializer
from vendor.models import Vendor

# Create your views here.


class PurchaseOrder(APIView):
    """
    API endpoint to handle purchase orders.
    """

    def post(self, request):
        """
        Create a new purchase order.

        Parameters:
        - request: HTTP POST request containing purchase order data.

        Returns:
        - Response: JSON response indicating success or failure of the operation.
        """
        try:
            data = request.data
            serializer = PurchaseOrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Purchase order created successfully",
                        "data": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get(self, request, po_id=None):
        """
        Retrieve purchase orders.

        Parameters:
        - request: HTTP GET request.
        - po_id: Optional parameter to filter purchase orders by PO number.

        Returns:
        - Response: JSON response containing purchase order data.
        """
        try:
            vendor_id = request.GET.get("vendor_id")
            if vendor_id:
                try:
                    # Check if the vendor_id exists
                    vendor = Vendor.objects.get(id=vendor_id)
                except Vendor.DoesNotExist:
                    # Return error response if vendor_id does not exist
                    return Response(
                        {"message": "Vendor order data does not exist"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
                # Filter orders with the specified vendor_id
                order_data = Order.objects.filter(vendor_id=vendor_id)
                serializer = PurchaseOrderSerializer(order_data, many=True)
                return Response(serializer.data)
            else:
                # If vendor_id is not provided, return all orders
                order_data = Order.objects.all()
                serializer = PurchaseOrderSerializer(order_data, many=True)
                return Response(serializer.data)
        except Exception as e:
            return Response(
                {"message": "Failed to retrieve the order details", "errors": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class PurchaseOrderDetailView(APIView):
    """
    API endpoint to handle individual purchase orders.
    """

    def get(self, request, po_id):
        """
        Retrieve details of a specific purchase order.

        Parameters:
        - request: HTTP GET request.
        - po_id: Purchase order number.

        Returns:
        - Response: JSON response containing purchase order details.
        """
        try:
            order = Order.objects.get(po_number=po_id)
            serializer = PurchaseOrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response(
                {"message": f"Order with PO number {po_id} does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"message": "Failed to retrieve the order details", "errors": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def put(self, request, po_id):
        """
        Update details of a specific purchase order.

        Parameters:
        - request: HTTP PUT request containing updated purchase order data.
        - po_id: Purchase order number.

        Returns:
        - Response: JSON response indicating success or failure of the operation.
        """
        try:
            order = Order.objects.get(po_number=po_id)
            data = request.data
            #if the status field is updated to complete mins po is Completed than set the po actual delivery time 
            if data['status'] =="Completed":
                order.po_delivered_on = timezone.now()
                order.save()

            serializer = PurchaseOrderSerializer(instance=order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Order details updated successfully",
                        "data": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {
                    "message": "Failed to update vendor details",
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"message": "Failed to update order details", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, request, po_id):
        """
        Delete a specific purchase order.

        Parameters:
        - request: HTTP DELETE request.
        - po_id: Purchase order number.

        Returns:
        - Response: JSON response indicating success or failure of the operation.
        """
        try:
            order = Order.objects.get(po_number=po_id)
            order.delete()
            return Response(
                {"message": "order deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Order.DoesNotExist:
            return Response(
                {"message": "order does not exist!"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"message": "Failed to delete Order", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
