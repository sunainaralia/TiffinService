from django.contrib import admin
from .models import (
    CategoryItem,
    Meal,
    DayPlan,
    WeeklyPlan,
    MenuItem,
    TodayMeal,
    Discount,
)


# Menu item register
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["id", "menu_name", "price", "image", "category", "kitchen_id"]


admin.site.register(MenuItem, MenuItemAdmin)


# weekly plan register
class CategoryItemAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "quantity")


class MealAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "meal_type",
    )


class DayPlanAdmin(admin.ModelAdmin):
    list_display = ("id", "day")


class WeeklyPlanAdmin(admin.ModelAdmin):
    list_display = ("id", "kitchen")


class TodayMealAdmin(admin.ModelAdmin):
    list_display = ("id", "kitchen", "time_of_day")


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
    ]


admin.site.register(CategoryItem)
admin.site.register(Meal, MealAdmin)
admin.site.register(DayPlan, DayPlanAdmin)
admin.site.register(WeeklyPlan, WeeklyPlanAdmin)
admin.site.register(TodayMeal, TodayMealAdmin)
admin.site.register(Discount, DiscountAdmin)
