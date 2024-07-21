from rest_framework import serializers
from decimal import Decimal
from datetime import datetime
from .models import (
    MenuItem,
    WeeklyPlan,
    TodayMeal,
    Discount,
    ScheduleOrder,
    Subscription,
    Order,
    CancellSubscription,
    CancelOrder
)
from ..Auth.models import OperatingHours,BusinessProfile
from django.utils.dateparse import parse_time
from ..payment.models import Payment
from ..Auth.serializers import UserProfileSerializer
from datetime import timedelta


# serializer for menu item
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            "id",
            "menu_name",
            "price",
            "image",
            "category",
            "kitchen_id",
            "is_active",
        ]


# today's meal serializer
class TodayMealSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(), many=True
    )

    class Meta:
        model = TodayMeal
        fields = ["id", "kitchen", "menu", "times_of_day", "created_at", "updated_at"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["menu"] = MenuItemSerializer(instance.menu.all(), many=True).data
        return representation

# discount serializers

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = [
            "id",
            "name",
            "banner",
            "coupan_code",
            "description",
            "valid_from",
            "valid_to",
            "discount_value",
            "discount_unit",
            "total_uses",
            "uses_per_customer",
            "minimum_spend_value",
            "created_at",
            "updated_at",
            "flag",
            "users",
        ]


# schedule serializer
class ScheduleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleOrder
        fields = ["id", "kitchen", "breakfast", "lunch", "dinner"]


# serializer for subscription
class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = [
            "id",
            "customer",
            "plan",
            "start_date",
            "end_date",
            "auto_renew",
            "meal_price",
            "meal_quantity",
            "schedule",
            "total_meal_price",
            "created_at",
            "updated_at",
            "is_active",
            "breakfast",
            "lunch",
            "dinner",
            "discount",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["schedule"] = ScheduleOrderSerializer(instance.schedule).data
        representation["customer"] = UserProfileSerializer(instance.customer).data
        return representation

    def create(self, validated_data):
        meal_price = validated_data.get("meal_price", 0)
        meal_quantity = validated_data.get("meal_quantity", 0)
        discount = validated_data.get("discount", 0)
        validated_data["total_meal_price"] = (meal_price * meal_quantity) - discount
        start_date = validated_data.get("start_date")
        if start_date is None:
            start_date = datetime.now()
        validated_data["start_date"] = start_date
        validated_data["end_date"] = start_date + timedelta(days=30)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.meal_price = validated_data.get("meal_price", instance.meal_price)
        instance.meal_quantity = validated_data.get(
            "meal_quantity", instance.meal_quantity
        )
        instance.discount = validated_data.get("discount", instance.discount)

        instance.total_meal_price = (
            instance.meal_price * instance.meal_quantity
        ) - instance.discount
        start_date = validated_data.get("start_date", instance.start_date)
        instance.start_date = start_date
        instance.end_date = start_date + timedelta(days=30)
        instance.save()
        return super().update(instance, validated_data)


# serializer for weekly plan
class WeeklyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyPlan
        fields = "__all__"


# serializer for order
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def validate(self, data):
        current_time = datetime.now().time()
        kitchen_id = data["kitchen"].id
        schedule = self.context["schedule"]

        def parse_schedule_time(time_str):
            if time_str is None:
                raise serializers.ValidationError("Schedule time is missing.")
            return datetime.strptime(time_str, "%I:%M %p").time()

        def parse_operating_hours(hours_str):
            if hours_str.lower() == "closed":
                return None, None
            try:
                start_time_str, end_time_str = hours_str.split(" - ")
                start_time = datetime.strptime(start_time_str, "%I:%M %p").time()
                end_time = datetime.strptime(end_time_str, "%I:%M %p").time()
                return start_time, end_time
            except ValueError:
                raise serializers.ValidationError("Invalid operating hours format.")

        # Retrieve operating hours
        operating_hours = OperatingHours.objects.filter(kitchen_id=kitchen_id).first()
        if not operating_hours:
            raise serializers.ValidationError(
                "Operating hours not found for this kitchen."
            )

        today = datetime.now().strftime("%A").lower()
        operating_hours_today = getattr(operating_hours, today)
        operating_start, operating_end = parse_operating_hours(operating_hours_today)
        if operating_start is None or operating_end is None:
            raise serializers.ValidationError("The kitchen is closed today.")
        if not (operating_start <= current_time <= operating_end):
            raise serializers.ValidationError("The kitchen is currently closed.")

        try:
            breakfast_start = parse_schedule_time(schedule["breakfast"]["start_time"])
            breakfast_end = parse_schedule_time(schedule["breakfast"]["end_time"])
            lunch_start = parse_schedule_time(schedule["lunch"]["start_time"])
            lunch_end = parse_schedule_time(schedule["lunch"]["end_time"])
            dinner_start = parse_schedule_time(schedule["dinner"]["start_time"])
            dinner_end = parse_schedule_time(schedule["dinner"]["end_time"])
        except KeyError as e:
            raise serializers.ValidationError(f"Missing schedule time: {e}")
        except ValueError as e:
            raise serializers.ValidationError(f"Invalid time format: {e}")

        # Determine meal time
        if breakfast_start <= current_time <= breakfast_end:
            meal_time = "breakfast"
        elif lunch_start <= current_time <= lunch_end:
            meal_time = "lunch"
        elif dinner_start <= current_time <= dinner_end:
            meal_time = "dinner"
        else:
            raise serializers.ValidationError("No orders can be placed at this time.")

        # Check weekly plan
        today = datetime.now().strftime("%A").lower()
        weekly_plan = WeeklyPlan.objects.filter(kitchen_id=kitchen_id).first()
        if not weekly_plan:
            raise serializers.ValidationError("Weekly plan not found for this kitchen.")

        daily_plan = next(
            (plan for plan in weekly_plan.plans if plan["day"] == today), None
        )
        if not daily_plan or meal_time not in daily_plan:
            raise serializers.ValidationError(
                "No meal plan available for the current time."
            )
        data["menu"] = weekly_plan

        return data

    def create(self, validated_data):
        menu = validated_data.pop("menu")
        order = super().create(validated_data)
        order.menu = menu
        order.save()
        return order

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        today = datetime.now().strftime("%A").lower()
        daily_plan = next(
            (plan for plan in instance.menu.plans if plan["day"] == today), None
        )
        meal_time = "dinner"  # This should be set dynamically based on current time
        representation["menu"] = {meal_time: daily_plan[meal_time]}
        return representation


# serializer for check discount availability
class CheckDiscountAvailabilitySerializer(serializers.Serializer):
    coupon_code = serializers.CharField(max_length=100, required=False)
    customer = serializers.IntegerField()
    # kitchen=serializers.IntegerField()

    def validate(self, data):
        coupon_code = data.get("coupon_code")
        if coupon_code:
            try:
                discount = Discount.objects.get(coupan_code=coupon_code, flag=True)
            except Discount.DoesNotExist:
                raise serializers.ValidationError("Invalid or expired coupon code.")
            if discount.valid_to < datetime.now().date():
                raise serializers.ValidationError("This coupon code has expired.")
            uses_per_customer = int(discount.uses_per_customer)

            customer_id = data["customer"]
            user_uses = discount.users.count(customer_id)
            if user_uses >= uses_per_customer:
                raise serializers.ValidationError(
                    "Coupon code usage limit reached for this customer."
                )
            discount = Discount.objects.get(coupan_code=coupon_code)
            customer_id = data.get("customer")
            users_list = discount.users
            users_list.append(customer_id)
            discount.users = users_list
            if len(users_list) >= int(discount.total_uses):
                discount.flag = False
            discount.save()
        data["discount"] = discount
        return data

# cancel subscription serializer
class CancellSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CancellSubscription
        fields = "__all__"
    def create(self, validated_data):
        subscription = validated_data["subscription"]
        if subscription:
            try:
                subscription = Subscription.objects.get(id=subscription.id)
            except Subscription.DoesNotExist:
                raise serializers.ValidationError("Subscription not found.")
            subscription.is_active=False
            subscription.end_date=datetime.now()
            subscription.save()

        return super().create(validated_data)


# cancel order serializer
class CancelOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CancelOrder
        fields = "__all__"
    def create(self, validated_data):
        subscription = validated_data.get("subscription")
        if subscription:
            try:
                subscription = Subscription.objects.get(id=subscription.id)
            except Subscription.DoesNotExist:
                raise serializers.ValidationError("Subscription not found.")
            cancel_time = validated_data['cancel_time']
            if cancel_time == "breakfast":
                subscription.breakfast +=1
            elif cancel_time == "lunch":
                subscription.lunch +=1
            elif cancel_time == "dinner":
                subscription.dinner +=1
            else:
                raise ValueError(
                    "Invalid cancel_time value. It must be 'breakfast', 'lunch', or 'dinner'."
                )
            subscription.save()
        order=validated_data["order"]
        if order:
            try:
                subscription = Subscription.objects.get(id=subscription.id)
            except Subscription.DoesNotExist:
                raise serializers.ValidationError("order not found.")
            order.order_status="Cancelled"
            order.save()

        return super().create(validated_data)
