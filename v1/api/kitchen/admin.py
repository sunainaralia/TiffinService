from django.contrib import admin
from .models import (
    WeeklyPlan,
    MenuItem,
    TodayMeal,
    Discount,
    ScheduleOrder,
    Subscription,
    CancellSubscription,
    CancelOrder,Order
)


# Menu item register
class MenuItemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "menu_name",
        "price",
        "image",
        "category",
        "kitchen_id",
        "is_active",
    ]


admin.site.register(MenuItem, MenuItemAdmin)


# today's meal admin
class TodayMealAdmin(admin.ModelAdmin):
    list_display = ("id", "kitchen", "times_of_day")


# discount admin
class DiscountAdmin(admin.ModelAdmin):
    list_display = [
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


# weekly plan admin
class WeeklyPlanAdmin(admin.ModelAdmin):
    list_display = ["id", "kitchen", "plans", "created_at", "updated_at"]


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["id", "kitchen", "breakfast", "lunch", "dinner"]


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [
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


# admin for cancell subscription
class CancellSubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "time",
        "user",
        "kitchen",
        "subscription",
        "reason",
        "cancel_time",

    )


admin.site.register(WeeklyPlan, WeeklyPlanAdmin)
admin.site.register(TodayMeal, TodayMealAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(ScheduleOrder, ScheduleAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(CancellSubscription,CancellSubscriptionAdmin)


@admin.register(CancelOrder)
class CancelOrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order_type",
        "reason",
        "kitchen",
        "user",
        "subscription",
        "time",
        "cancel_time",
        "order",
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "kitchen",
        "customer",
        "extra",
        "menu",
        "meal_price",
        "meal_quantity",
        "addon_price",
        "discount",
        "total_meal_price",
        "order_status",
        "payment",
        "schedule",
        "createdAt",
        "updatedAt",
    ]
