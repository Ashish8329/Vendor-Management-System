from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from vendor.models import Vendor
from rest_framework.permissions import IsAuthenticated
from .serializers import VendorSerializer

# Create your views here.


class Vendors(APIView):
    """API endpoint for managing vendors."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Create a new vendor."""
        data = request.data
        serializer = VendorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Vendor created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Failed to create vendor", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, vendor_id=None):
        """Retrieve all vendors or the details of a specific vendor."""
        try:
            if vendor_id is not None:
                # If vendor_id is provided, retrieve the details of the specific vendor
                vendor = Vendor.objects.get(pk=vendor_id)
                serializer = VendorSerializer(vendor)
                return Response(serializer.data)
            else:
                # If no vendor_id is provided, retrieve all vendors
                vendors = Vendor.objects.all()
                serializer = VendorSerializer(vendors, many=True)
                return Response(serializer.data)
        except Vendor.DoesNotExist:
            return Response(
                {"message": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"message": "Failed to retrieve vendors", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def put(self, request, vendor_id=None):
        """Update the details of a specific vendor."""
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            serializer = VendorSerializer(instance=vendor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Vendor details updated successfully",
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
        except Vendor.DoesNotExist:
            return Response(
                {"message": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"message": "Failed to update vendor details", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, request, vendor_id):
        """Delete a specific vendor."""
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            vendor.delete()
            return Response(
                {"message": "Vendor deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Vendor.DoesNotExist:
            return Response(
                {"message": "Vendor does not exist!"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"message": "Failed to delete vendor", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )