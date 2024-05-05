from django.urls import include, path
from order.views import PurchaseOrder, PurchaseOrderDetailView
from performance_history.views import VendorPerformanceAPIView
from vendor.views import Vendors
from vms_auth.views import RegisterUser, UserLogin

urlpatterns = [
    path("register/", RegisterUser.as_view()),
    path("login/", UserLogin.as_view()),
    path("vendors/", Vendors.as_view()),
    path("vendors/<int:vendor_id>/", Vendors.as_view()),
    path("purchase_orders/", PurchaseOrder.as_view()),
    path("purchase_orders/<int:po_id>/", PurchaseOrderDetailView.as_view()),
    path("vendors/<int:vendor_id>/performance/", VendorPerformanceAPIView.as_view()),
]
