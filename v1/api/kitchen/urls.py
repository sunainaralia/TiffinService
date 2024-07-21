from django.urls import path
from .views import (
    MenuItemView,
    WeeklyPlanView,
    TodayMealView,
    DiscountView,
    ScheduleOrderView,
    SubscriptionView,
    OrderView,
    CheckDiscountEligibilityView,
    CancellSubscriptionView,
    CancelOrderView,
)

urlpatterns = [
    path("menu/", MenuItemView.as_view(), name="MenuItem"),
    path("menu/<pk>/", MenuItemView.as_view()),
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
    path("order/", OrderView.as_view(), name="order"),
    path("order/<int:pk>/", OrderView.as_view(), name="order-detail"),
    path(
        "check-discount/",
        CheckDiscountEligibilityView.as_view(),
        name="CheckDiscountEligibility",
    ),
    path(
        "cancel-subscriptions/",
        CancellSubscriptionView.as_view(),
        name="cancel_subscription_list_create",
    ),
    path(
        "cancel-subscriptions/<int:pk>/",
        CancellSubscriptionView.as_view(),
        name="cancel_subscription_detail",
    ),
    path("cancel-orders/", CancelOrderView.as_view(), name="cancel_order_list_create"),
    path(
        "cancel-orders/<int:pk>/", CancelOrderView.as_view(), name="cancel_order_detail"
    ),
]
