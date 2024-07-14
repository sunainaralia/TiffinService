from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem,WeeklyPlan,CategoryItem,DayPlan,Meal,TodayMeal,Discount,ScheduleOrder,Subscription,ExtraMeal
from .serializers import (
    MenuItemSerializer,
    WeeklyPlanSerializer,
    CategoryItemSerializer,
    MealSerializer,
    DayPlanSerializer,
    TodayMealSerializer,
    DiscountSerializer,
    ScheduleOrderSerializer,
    SubscriptionSerializer,
    ExtraMealSerializer
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


# category items view
class CategoryItemView(APIView):
    permission_classes = [IsAuthenticatedOrAllowedGet]

    def post(self, request, format=None):
        serializer = CategoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Category item created successfully.",
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
                category_item = CategoryItem.objects.get(pk=pk)
                serializer = CategoryItemSerializer(category_item)
                return Response(
                    {
                        "success": True,
                        "msg": "Category item retrieved successfully.",
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except CategoryItem.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Category item not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            category_items = CategoryItem.objects.all()
            serializer = CategoryItemSerializer(category_items, many=True)
            return Response(
                {
                    "success": True,
                    "msg": "Category items retrieved successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            category_item = CategoryItem.objects.get(pk=pk)
        except CategoryItem.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Category item not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CategoryItemSerializer(
            category_item, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Category item updated successfully.",
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
            category_item = CategoryItem.objects.get(pk=pk)
            category_item.delete()
            return Response(
                {
                    "success": True,
                    "msg": "Category item deleted successfully.",
                    "status": status.HTTP_204_NO_CONTENT,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except CategoryItem.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Category item not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# View for Meal
class MealView(APIView):
    permission_classes = [IsAuthenticatedOrAllowedGet]

    def post(self, request, format=None):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            meal = serializer.save()
            meal_serializer = MealSerializer(meal)
            return Response(
                {
                    "success": True,
                    "msg": "Meal created successfully.",
                    "data": meal_serializer.data,
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
                meal = Meal.objects.get(pk=pk)
                serializer = MealSerializer(meal)
                return Response(
                    {
                        "success": True,
                        "msg": "Meal retrieved successfully.",
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except Meal.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Meal not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            meals = Meal.objects.all()
            serializer = MealSerializer(meals, many=True)
            return Response(
                {
                    "success": True,
                    "msg": "Meals retrieved successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            meal = Meal.objects.get(pk=pk)
        except Meal.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Meal not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MealSerializer(meal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Meal updated successfully.",
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
            meal = Meal.objects.get(pk=pk)
            meal.delete()
            return Response(
                {
                    "success": True,
                    "msg": "Meal deleted successfully.",
                    "status": status.HTTP_204_NO_CONTENT,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except Meal.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Meal not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# View for DayPlan
class DayPlanView(APIView):
    permission_classes = [IsAuthenticatedOrAllowedGet]

    def post(self, request, format=None):
        serializer = DayPlanSerializer(data=request.data)
        if serializer.is_valid():
            day_plan = serializer.save()
            day_plan_serializer = DayPlanSerializer(day_plan)
            return Response(
                {
                    "success": True,
                    "msg": "Day plan created successfully.",
                    "data": day_plan_serializer.data,
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
                day_plan = DayPlan.objects.get(pk=pk)
                serializer = DayPlanSerializer(day_plan)
                return Response(
                    {
                        "success": True,
                        "msg": "Day plan retrieved successfully.",
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except DayPlan.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Day plan not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            day_plans = DayPlan.objects.all()
            serializer = DayPlanSerializer(day_plans, many=True)
            return Response(
                {
                    "success": True,
                    "msg": "Day plans retrieved successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            day_plan = DayPlan.objects.get(pk=pk)
        except DayPlan.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Day plan not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = DayPlanSerializer(day_plan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Day plan updated successfully.",
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
            day_plan = DayPlan.objects.get(pk=pk)
            day_plan.delete()
            return Response(
                {
                    "success": True,
                    "msg": "Day plan deleted successfully.",
                    "status": status.HTTP_204_NO_CONTENT,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except DayPlan.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Day plan not found.",
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


# view for extra meal
class ExtraMealView(APIView):
    def post(self, request, format=None):
        serializer = ExtraMealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Extra meal created successfully.",
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
                extra_meal = ExtraMeal.objects.get(pk=pk)
                serializer = ExtraMealSerializer(extra_meal)
                return Response(
                    {
                        "success": True,
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except ExtraMeal.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Extra meal not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            extra_meals = ExtraMeal.objects.all()
            serializer = ExtraMealSerializer(extra_meals, many=True)
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
            extra_meal = ExtraMeal.objects.get(pk=pk)
        except ExtraMeal.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Extra meal not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ExtraMealSerializer(extra_meal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Extra meal updated successfully.",
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
            extra_meal = ExtraMeal.objects.get(pk=pk)
        except ExtraMeal.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Extra meal not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        extra_meal.delete()
        return Response(
            {
                "success": True,
                "msg": "Extra meal deleted successfully.",
                "status": status.HTTP_204_NO_CONTENT,
            },
            status=status.HTTP_204_NO_CONTENT,
        )
