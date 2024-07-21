from django.db import models
from ..Auth.models import BusinessProfile,UserProfile,OperatingHours
from ..payment.models import Payment
# Create your models here.
class MenuItem(models.Model):
    kitchen_id = models.ForeignKey(
        BusinessProfile, on_delete=models.CASCADE, related_name="menu"
    )
    menu_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=200,null=True,blank=True) 
    category = models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.menu_name


# discount model
class Discount(models.Model):
    name=models.CharField(max_length=100)
    banner=models.CharField(max_length=200,null=True)
    coupan_code=models.CharField(max_length=100)
    description=models.TextField()
    valid_from=models.DateField()
    valid_to=models.DateField()
    discount_value=models.CharField(max_length=100)
    discount_unit=models.CharField(max_length=100)
    total_uses=models.CharField(max_length=100)
    uses_per_customer=models.CharField(max_length=100)
    minimum_spend_value=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    flag=models.BooleanField(default=True)
    users=models.JSONField(default=list)


# schedule of order timing
class ScheduleOrder(models.Model):
    kitchen = models.ForeignKey(BusinessProfile,on_delete=models.CASCADE,related_name='schedule')
    breakfast=models.JSONField(default=dict)
    lunch=models.JSONField(default=dict)
    dinner=models.JSONField(default=dict)


# subscription model
class Subscription(models.Model):
    customer = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE
    ) 
    kitchen=models.ForeignKey(BusinessProfile,on_delete=models.CASCADE,null=True)
    plan = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    auto_renew = models.BooleanField(default=False)
    meal_price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_quantity = models.IntegerField()
    schedule = models.ForeignKey(ScheduleOrder,on_delete=models.CASCADE,related_name="scheduled_subscription",null=True)
    discount=models.FloatField(default=0)
    total_meal_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,related_name="subscription",null=True)
    breakfast=models.IntegerField(default=0)
    lunch=models.IntegerField(default=0)
    dinner=models.IntegerField(default=0)


# today's meal
class TodayMeal(models.Model):
    kitchen = models.ForeignKey(
        BusinessProfile, on_delete=models.CASCADE, related_name="today_meal"
    )
    times_of_day = models.CharField(max_length=100, null=True)
    menu = models.ManyToManyField(MenuItem, related_name="today_meal_menu")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


# weekly plan
class WeeklyPlan(models.Model):
    kitchen=models.ForeignKey(BusinessProfile,on_delete=models.CASCADE,related_name='Weekly_plan')
    plans=models.JSONField(default=list)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)


# order model
class Order(models.Model):
    kitchen = models.ForeignKey(
        BusinessProfile, related_name="kitchen_orders", on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        UserProfile, related_name="customer_orders", on_delete=models.CASCADE
    )
    extra = models.JSONField(default=list)
    menu = models.ForeignKey(
        WeeklyPlan, on_delete=models.CASCADE, related_name="order_menu",null=True
    )
    meal_price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_quantity = models.IntegerField()
    addon_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    total_meal_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(
        max_length=100
    )  # "Delivered", "Cancelled", or "Processing"
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="order_payment"
    )
    schedule = models.ForeignKey(ScheduleOrder,on_delete=models.CASCADE,related_name="order")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


# cancell subscription model
class CancellSubscription(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    kitchen=models.ForeignKey(BusinessProfile,on_delete=models.CASCADE)
    subscription=models.ForeignKey(Subscription,on_delete=models.CASCADE)
    reason=models.TextField()
    cancel_time=models.CharField(max_length=100)

# cancel order model
class CancelOrder(models.Model):
    order_type=models.CharField(max_length=100)
    reason=models.TextField()
    kitchen = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE,null=True)
    time=models.DateTimeField(auto_now_add=True)
    cancel_time=models.CharField(max_length=100)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True,related_name="cancel_order")
