from django.urls import path
from .views import PaymentView

urlpatterns = [
    path("payments/", PaymentView.as_view(), name="payment-list-create"),
    path("payments/<int:pk>/", PaymentView.as_view(), name="payment-detail"),
]
