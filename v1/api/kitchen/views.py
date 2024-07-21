from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem,WeeklyPlan,TodayMeal,Discount,ScheduleOrder,Subscription,Order,CancellSubscription,CancelOrder
from .serializers import (
    MenuItemSerializer,
    WeeklyPlanSerializer,
    TodayMealSerializer,
    DiscountSerializer,
    ScheduleOrderSerializer,
    SubscriptionSerializer,
    OrderSerializer,
    CheckDiscountAvailabilitySerializer,
    CancellSubscriptionSerializer,
    CancelOrderSerializer

)
from ...customPermission import IsAuthenticatedOrAllowedGet

# views for menu item
class MenuItemView(APIView):
    permission_classes = [IsAuthenticatedOrAllowedGet]

    def post(self, request, format=None):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Menu item created successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                menu_item = MenuItem.objects.get(pk=pk)
                serializer = MenuItemSerializer(menu_item)
                return Response(
                    {
                        "success": True,
                        "msg": "Menu item retrieved successfully.",
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except MenuItem.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Menu item not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            menu_items = MenuItem.objects.all()
            serializer = MenuItemSerializer(menu_items, many=True)
            return Response(
                {
                    "success": True,
                    "msg": "Menu items retrieved successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            menu_item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Menu item not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MenuItemSerializer(menu_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Menu item updated successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        try:
            menu_item = MenuItem.objects.get(pk=pk)
            menu_item.delete()
            return Response(
                {
                    "success": True,
                    "msg": "Menu item deleted successfully.",
                    "status": status.HTTP_204_NO_CONTENT,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except MenuItem.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Menu item not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# view for weekly plan
class WeeklyPlanView(APIView):
    permission_classes = [IsAuthenticatedOrAllowedGet]

    def post(self, request, format=None):
        serializer = WeeklyPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Weekly plan created successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                weekly_plan = WeeklyPlan.objects.get(pk=pk)
                serializer = WeeklyPlanSerializer(weekly_plan)
                return Response(
                    {
                        "success": True,
                        "msg": "Weekly plan retrieved successfully.",
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except WeeklyPlan.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Weekly plan not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            weekly_plans = WeeklyPlan.objects.all()
            serializer = WeeklyPlanSerializer(weekly_plans, many=True)
            return Response(
                {
                    "success": True,
                    "msg": "Weekly plans retrieved successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            weekly_plan = WeeklyPlan.objects.get(pk=pk)
        except WeeklyPlan.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Weekly plan not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = WeeklyPlanSerializer(weekly_plan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Weekly plan updated successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        try:
            weekly_plan = WeeklyPlan.objects.get(pk=pk)
            weekly_plan.delete()
            return Response(
                {
                    "success": True,
                    "msg": "Weekly plan deleted successfully.",
                    "status": status.HTTP_204_NO_CONTENT,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except WeeklyPlan.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Weekly plan not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# views for today's meal plan
class TodayMealView(APIView):
    permission_classes = [IsAuthenticatedOrAllowedGet]

    def post(self, request, format=None):
        serializer = TodayMealSerializer(data=request.data)
        if serializer.is_valid():
            today_meal = serializer.save()
            today_meal_serializer = TodayMealSerializer(today_meal)
            return Response(
                {
                    "success": True,
                    "msg": "Today's meal created successfully.",
                    "data": today_meal_serializer.data,
                    "status": status.HTTP_201_CREATED,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                today_meal = TodayMeal.objects.get(pk=pk)
                serializer = TodayMealSerializer(today_meal)
                return Response(
                    {
                        "success": True,
                        "msg": "Today's meal retrieved successfully.",
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except TodayMeal.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Today's meal not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            today_meals = TodayMeal.objects.all()
            serializer = TodayMealSerializer(today_meals, many=True)
            return Response(
                {
                    "success": True,
                    "msg": "Today's meals retrieved successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            today_meal = TodayMeal.objects.get(pk=pk)
        except TodayMeal.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Today's meal not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = TodayMealSerializer(today_meal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Today's meal updated successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        try:
            today_meal = TodayMeal.objects.get(pk=pk)
            today_meal.delete()
            return Response(
                {
                    "success": True,
                    "msg": "Today's meal deleted successfully.",
                    "status": status.HTTP_204_NO_CONTENT,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except TodayMeal.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Today's meal not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# discount view
class DiscountView(APIView):
    def post(self, request, format=None):
        serializer = DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Discount created successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                discount = Discount.objects.get(pk=pk)
                serializer = DiscountSerializer(discount)
                return Response(
                    {
                        "success": True,
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except Discount.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Discount not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            discounts = Discount.objects.all()
            serializer = DiscountSerializer(discounts, many=True)
            return Response(
                {
                    "success": True,
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            discount = Discount.objects.get(pk=pk)
        except Discount.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Discount not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = DiscountSerializer(discount, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Discount updated successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        try:
            discount = Discount.objects.get(pk=pk)
        except Discount.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Discount not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        discount.delete()
        return Response(
            {
                "success": True,
                "msg": "Discount deleted successfully.",
                "status": status.HTTP_204_NO_CONTENT,
            },
            status=status.HTTP_204_NO_CONTENT,
        )


# view for schedule timing
class ScheduleOrderView(APIView):
    def post(self, request, format=None):
        serializer = ScheduleOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Schedule order created successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                schedule_order = ScheduleOrder.objects.get(pk=pk)
                serializer = ScheduleOrderSerializer(schedule_order)
                return Response(
                    {
                        "success": True,
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except ScheduleOrder.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Schedule order not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            schedule_orders = ScheduleOrder.objects.all()
            serializer = ScheduleOrderSerializer(schedule_orders, many=True)
            return Response(
                {
                    "success": True,
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            schedule_order = ScheduleOrder.objects.get(pk=pk)
        except ScheduleOrder.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Schedule order not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ScheduleOrderSerializer(
            schedule_order, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Schedule order updated successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        try:
            schedule_order = ScheduleOrder.objects.get(pk=pk)
        except ScheduleOrder.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Schedule order not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        schedule_order.delete()
        return Response(
            {
                "success": True,
                "msg": "Schedule order deleted successfully.",
                "status": status.HTTP_204_NO_CONTENT,
            },
            status=status.HTTP_204_NO_CONTENT,
        )


# view for subscription
class SubscriptionView(APIView):
    def post(self, request, format=None):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Meal plan created successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                meal_plan = Subscription.objects.get(pk=pk)
                serializer = SubscriptionSerializer(meal_plan)
                return Response(
                    {
                        "success": True,
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except Subscription.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Meal plan not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            meal_plans = Subscription.objects.all()
            serializer = SubscriptionSerializer(meal_plans, many=True)
            return Response(
                {
                    "success": True,
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            meal_plan = Subscription.objects.get(pk=pk)
        except Subscription.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Meal plan not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = SubscriptionSerializer(meal_plan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Meal plan updated successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        try:
            meal_plan = Subscription.objects.get(pk=pk)
        except Subscription.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Meal plan not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        meal_plan.delete()
        return Response(
            {
                "success": True,
                "msg": "Meal plan deleted successfully.",
                "status": status.HTTP_204_NO_CONTENT,
            },
            status=status.HTTP_204_NO_CONTENT,
        )


# view for order
class OrderView(APIView):

    def post(self, request, format=None):
        # Fetch the schedule data using the provided ID
        schedule_id = request.data.get("schedule")
        if not schedule_id:
            return Response(
                {
                    "success": False,
                    "msg": "Schedule ID is required.",
                    "status": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            schedule = ScheduleOrder.objects.get(id=schedule_id)
        except ScheduleOrder.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Schedule not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        # Serialize the schedule data
        schedule_serializer = ScheduleOrderSerializer(schedule)
        schedule_data = schedule_serializer.data

        serializer_context = {"schedule": schedule_data}
        serializer = OrderSerializer(data=request.data, context=serializer_context)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Order created successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                order = Order.objects.get(pk=pk)
                serializer = OrderSerializer(order)
                return Response(
                    {
                        "success": True,
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except Order.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Order not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(
                {
                    "success": True,
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Order not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Order updated successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Order not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        order.delete()
        return Response(
            {
                "success": True,
                "msg": "Order deleted successfully.",
                "status": status.HTTP_204_NO_CONTENT,
            },
            status=status.HTTP_204_NO_CONTENT,
        )


# check is discount is eligible
class CheckDiscountEligibilityView(APIView):
    def post(self, request, format=None):
        serializer = CheckDiscountAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            discount_serializer = DiscountSerializer(validated_data.get("discount"))
            response_data = (
                discount_serializer.data if validated_data.get("discount") else {}
            )
            return Response(
                {
                    "success": True,
                    "msg": "Discount check completed successfully.",
                    "data": response_data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


# cancel subscription

class CancellSubscriptionView(APIView):
    def post(self, request, format=None):
        serializer = CancellSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Cancellation subscription created successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                cancell_subscription = CancellSubscription.objects.get(pk=pk)
                serializer = CancellSubscriptionSerializer(cancell_subscription)
                return Response(
                    {
                        "success": True,
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except CancellSubscription.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Cancellation subscription not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            cancell_subscriptions = CancellSubscription.objects.all()
            serializer = CancellSubscriptionSerializer(cancell_subscriptions, many=True)
            return Response(
                {
                    "success": True,
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            cancell_subscription = CancellSubscription.objects.get(pk=pk)
        except CancellSubscription.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Cancellation subscription not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CancellSubscriptionSerializer(
            cancell_subscription, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Cancellation subscription updated successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        try:
            cancell_subscription = CancellSubscription.objects.get(pk=pk)
        except CancellSubscription.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Cancellation subscription not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        cancell_subscription.delete()
        return Response(
            {
                "success": True,
                "msg": "Cancellation subscription deleted successfully.",
                "status": status.HTTP_204_NO_CONTENT,
            },
            status=status.HTTP_204_NO_CONTENT,
        )


# cancel order views
class CancelOrderView(APIView):
    def post(self, request, format=None):
        serializer = CancelOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Cancel order created successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                cancel_order = CancelOrder.objects.get(pk=pk)
                serializer = CancelOrderSerializer(cancel_order)
                return Response(
                    {
                        "success": True,
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except CancelOrder.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Cancel order not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            cancel_orders = CancelOrder.objects.all()
            serializer = CancelOrderSerializer(cancel_orders, many=True)
            return Response(
                {
                    "success": True,
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            cancel_order = CancelOrder.objects.get(pk=pk)
        except CancelOrder.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Cancel order not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CancelOrderSerializer(
            cancel_order, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Cancel order updated successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "msg": "Invalid data.",
                "status": status.HTTP_400_BAD_REQUEST,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        try:
            cancel_order = CancelOrder.objects.get(pk=pk)
        except CancelOrder.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Cancel order not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        cancel_order.delete()
        return Response(
            {
                "success": True,
                "msg": "Cancel order deleted successfully.",
                "status": status.HTTP_204_NO_CONTENT,
            },
            status=status.HTTP_204_NO_CONTENT,
        )
