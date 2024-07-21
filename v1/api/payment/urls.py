from django.urls import path
from .views import PaymentView

urlpatterns = [
    path("payment/", PaymentView.as_view(), name="payment-list-create"),
    path("payment/<int:pk>/", PaymentView.as_view(), name="payment-detail"),
]
