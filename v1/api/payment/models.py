from django.db import models
from ..Auth.models import UserProfile,BusinessProfile
# Create your models here.
class Payment(models.Model):
    payment_method = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="payments"
    )
    kitchen=models.ForeignKey(BusinessProfile,on_delete=models.CASCADE,related_name="payment",null=True)
    def __str__(self):
        return f"{self.user.username} - {self.payment_method} - {self.payment_status}"
