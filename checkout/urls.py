from django.urls import path
from .views import checkout, checkout_success, checkout_cancelled

urlpatterns = [
    path('', checkout),
    path('success', checkout_success, name='checkout_success'),
    path('cancelled', checkout_cancelled, name='checkout_cancelled')
    ]