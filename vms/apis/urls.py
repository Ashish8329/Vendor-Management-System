from django.urls import path, include
from vms_auth.views import RegisterUser, UserLogin

urlpatterns = [
    path('register/',RegisterUser.as_view()),
    path('login/',UserLogin.as_view()),
]