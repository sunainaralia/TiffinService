from django.db import models
from ..Auth.models import BusinessProfile,UserProfile
# Create your models here.
class MenuItem(models.Model):
    kitchen_id = models.ForeignKey(
        BusinessProfile, on_delete=models.CASCADE, related_name="menu"
    )
    menu_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=200,null=True,blank=True) 
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.menu_name


# weekly plan

class CategoryItem(models.Model):
    category = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.category} - {self.quantity}"


class Meal(models.Model):
    meal_type = models.CharField(max_length=50)
    items = models.ManyToManyField(CategoryItem, related_name="meals")

    def __str__(self):
        return self.meal_type


class DayPlan(models.Model):
    day = models.CharField(max_length=10)
    breakfast = models.ForeignKey(
        Meal, related_name="breakfast_dayplans", on_delete=models.CASCADE
    )
    lunch = models.ForeignKey(
        Meal, related_name="lunch_dayplans", on_delete=models.CASCADE
    )
    dinner = models.ForeignKey(
        Meal, related_name="dinner_dayplans", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.day


class WeeklyPlan(models.Model):
    kitchen = models.ForeignKey(
        BusinessProfile, on_delete=models.CASCADE, related_name="weekly_plans"
    )
    plans = models.ManyToManyField(DayPlan, related_name="weekly_plans")

    def __str__(self):
        return f"Weekly Plan for {self.kitchen.kitchenName}"


#  today meal
class TodayMeal(models.Model):
    kitchen = models.ForeignKey(
        BusinessProfile, on_delete=models.CASCADE, related_name="today_meal"
    )
    time_of_day=models.CharField(max_length=100)
    menu=models.ManyToManyField(MenuItem,related_name="today_meal")

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


# schedule of order timing
class ScheduleOrder(models.Model):
    kitchen = models.ForeignKey(BusinessProfile,on_delete=models.CASCADE,related_name='schedule')
    time_of_day=models.CharField(max_length=100)
    start_time=models.TimeField()
    end_time=models.TimeField()
    def __str__(self):
        return f"{self.kitchen} - {self.time_of_day} ({self.start_time} to {self.end_time})"


# subscription model
class Subscription(models.Model):
    customer = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE
    ) 
    kitchen=models.ForeignKey(BusinessProfile,on_delete=models.CASCADE,null=True)
    plan = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    auto_renew = models.BooleanField(default=False)
    meal_price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_quantity = models.IntegerField()
    schedule = models.ForeignKey(
        ScheduleOrder, on_delete=models.CASCADE, related_name="meal_plans"
    )
    discount = models.ForeignKey(
        Discount, on_delete=models.CASCADE, related_name="meal_plans"
    )
    total_meal_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.customer} - {self.plan} ({self.start_date} to {self.end_date})"


# extra meal
class ExtraMeal(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

    @property
    def price(self):
        try:
            menu_item = MenuItem.objects.get(menu_name=self.item)
            return menu_item.price
        except MenuItem.DoesNotExist:
            return None
