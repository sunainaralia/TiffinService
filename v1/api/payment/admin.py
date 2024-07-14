from django.contrib import admin
from .models import Payment


# payment admin
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "payment_method",
        "payment_status",
        "created_at",
        "updated_at",
        "order",
        "user",
    ]
admin.site.register(Payment,PaymentAdmin)