from django.urls import path
from .views import (
    MenuItemView,
    WeeklyPlanView,
    CategoryItemView,
    MealView,
    DayPlanView,
    TodayMealView,
    DiscountView,
    ScheduleOrderView,
    SubscriptionView,
    ExtraMealView
)

urlpatterns = [
    path("menu/", MenuItemView.as_view(), name="MenuItem"),
    path("menu/<pk>/", MenuItemView.as_view()),
    path("category-item/", CategoryItemView.as_view(), name="category-item"),
    path("meal/", MealView.as_view(), name="meal"),
    path("day-plan/", DayPlanView.as_view(), name="day-plan"),
    path("weeklyplan/", WeeklyPlanView.as_view(), name="weeklyplan"),
    path("weeklyplan/<int:pk>/", WeeklyPlanView.as_view(), name="weeklyplan-detail"),
    path("today-meal/", TodayMealView.as_view(), name="today-meal"),
    path("today-meal/<pk>/", TodayMealView.as_view(), name="today-meal-detail"),
    path("discounts/", DiscountView.as_view(), name="discount-list-create"),
    path("discounts/<int:pk>/", DiscountView.as_view(), name="discount-detail"),
    path(
        "schedule-orders/",
        ScheduleOrderView.as_view(),
        name="schedule-order-list-create",
    ),
    path(
        "schedule-orders/<int:pk>/",
        ScheduleOrderView.as_view(),
        name="schedule-order-detail",
    ),
    path("subscription/", SubscriptionView.as_view(), name="subscription-list-create"),
    path(
        "subscription/<int:pk>/", SubscriptionView.as_view(), name="subscription-detail"
    ),
    path("extra-meals/", ExtraMealView.as_view(), name="extra-meal-list-create"),
    path("extra-meals/<int:pk>/", ExtraMealView.as_view(), name="extra-meal-detail"),
]
