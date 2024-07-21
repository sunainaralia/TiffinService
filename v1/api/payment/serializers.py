from rest_framework import serializers
from .models import Payment
# serializer for payment
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "payment_method",
            "payment_status",
            "created_at",
            "updated_at",
            "user",
            "kitchen",
        ]
