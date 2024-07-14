from rest_framework import serializers
from .models import (
    MenuItem,
    CategoryItem,
    Meal,
    DayPlan,
    WeeklyPlan,
    TodayMeal,
    Discount,
    ScheduleOrder,
    Subscription,
    ExtraMeal
)


# serializer for menu item
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "menu_name", "price", "image", "category", "kitchen_id"]


# weekly plan serializers
class CategoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryItem
        fields = ["id", "category", "quantity"]


class MealSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        queryset=CategoryItem.objects.all(), many=True
    )

    class Meta:
        model = Meal
        fields = ["id", "meal_type", "items"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["items"] = CategoryItemSerializer(
            instance.items.all(), many=True
        ).data
        return representation


class DayPlanSerializer(serializers.ModelSerializer):
    breakfast = serializers.PrimaryKeyRelatedField(queryset=Meal.objects.all())
    lunch = serializers.PrimaryKeyRelatedField(queryset=Meal.objects.all())
    dinner = serializers.PrimaryKeyRelatedField(queryset=Meal.objects.all())

    class Meta:
        model = DayPlan
        fields = ["id", "day", "breakfast", "lunch", "dinner"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["breakfast"] = MealSerializer(instance.breakfast).data
        representation["lunch"] = MealSerializer(instance.lunch).data
        representation["dinner"] = MealSerializer(instance.dinner).data
        return representation


class WeeklyPlanSerializer(serializers.ModelSerializer):
    plans = serializers.PrimaryKeyRelatedField(
        queryset=DayPlan.objects.all(), many=True
    )

    class Meta:
        model = WeeklyPlan
        fields = ["id", "kitchen", "plans"]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["plans"] = DayPlanSerializer(instance.plans.all(),many=True).data
        return representation


# today's meal serializer
class TodayMealSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all(), many=True)

    class Meta:
        model = TodayMeal
        fields = ["id", "kitchen", "menu","time_of_day"]

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
        ]


# schedule serializer
class ScheduleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleOrder
        fields = ["id", "kitchen", "time_of_day", "start_time", "end_time"]


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
            "discount",
            "total_meal_price",
            "created_at",
            "updated_at",
            "is_active",
        ]

# serializer for extra meal
class ExtraMealSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = ExtraMeal
        fields = ["item", "quantity", "price"]
