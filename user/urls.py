from django.urls import path
from .views import RegistrationUserAPIView, LoginAPIView

urlpatterns = [
    path('user/registrations', RegistrationUserAPIView.as_view(), name='registrations'),
    path('user/login', LoginAPIView.as_view(), name='login'),
]




