from django.urls import include, path

from vendor.views import Vendors
from vms_auth.views import RegisterUser, UserLogin

urlpatterns = [
    path("register/", RegisterUser.as_view()),
    path("login/", UserLogin.as_view()),
    path("vendors/", Vendors.as_view()),
    path("vendors/<int:vendor_id>/", Vendors.as_view()),
]