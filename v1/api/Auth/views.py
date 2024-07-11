from .models import UserProfile,UserAddress,BusinessProfile,OperatingHours
from .serializers import UserProfileSerializer, UserLoginSerializer, AddressSerializer,BusinessProfileSerializer,OperatingHoursSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
import random
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

# genrate token manually
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {"access": str(refresh.access_token), "refress": str(refresh)}


# UserProfile view
class UserProfileView(APIView):
    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_token_for_user(user)
            return Response(
                {
                    "success": True,
                    "msg": "user is registered successfully",
                    "data": serializer.data,
                    "token": token,
                    "status": status.HTTP_201_CREATED,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {
                    "success": False,
                    "msg": serializer.errors,
                    "status": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


# api for send otp using mobile no
class SendOtpToMobileNo(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_no = request.data.get("phone_no")
            user = UserProfile.objects.filter(phone_no=phone_no).first()
            if user is not None:
                if not user.is_blocked:
                    return Response(
                        {
                            "success": True,
                            "msg": "otp is send to your mobile no,plz check",
                            "otp": random.randint(100000, 999999),
                            "uid": user.id,
                            "status": status.HTTP_200_OK,
                        },
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {
                            "success": False,
                            "msg": "you are blocked",
                            "status": status.HTTP_403_FORBIDDEN,
                        },
                        status=status.HTTP_403_FORBIDDEN,
                    )
            else:
                return Response(
                    {
                        "success": False,
                        "msg": "plz enter valid mobile no.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(
            {
                "msg": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST,
                "success": False,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


# login the user by verify the otp
class LoginUserView(APIView):
    def post(self, request, pk, otp, format=None):
        entered_otp = request.data.get("otp")
        try:
            user = UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            return Response(
                {"success": False, "msg": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if otp == entered_otp:
            user.recentLogin = timezone.now()
            user.save()

            serializer = UserProfileSerializer(user)
            token = get_token_for_user(user)
            return Response(
                {
                    "success": True,
                    "msg": "Login successful",
                    "token": token,
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {"success": False, "msg": "OTP is invalid"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# view for User Addrss details
class AddressView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        check_exist=UserAddress.objects.filter(user=request.data.get("user")).exists()
        if check_exist:
            return Response(
                {
                    "success": False,
                    "msg": "Address already exists.",
                    "status": status.HTTP_409_CONFLICT,
                },
                status=status.HTTP_409_CONFLICT,
            )
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Address created successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"success": False, "msg": "Invalid data.", "status": status.HTTP_400_BAD_REQUEST, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                address = UserAddress.objects.get(pk=pk)
                serializer = AddressSerializer(address)
                return Response(
                    {
                        "success": True,
                        "msg": "Address retrieved successfully.",
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except UserAddress.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Address not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            addresses = UserAddress.objects.all()
            serializer = AddressSerializer(addresses, many=True)
            return Response(
                {
                    "success": True,
                    "msg": "Addresses retrieved successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            address = UserAddress.objects.get(pk=pk)
        except UserAddress.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Address not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Address updated successfully.",
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
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        try:
            address = UserAddress.objects.get(pk=pk)
            address.delete()
            return Response(
                {
                    "success": True,
                    "msg": "Address deleted successfully.",
                    "status": status.HTTP_204_NO_CONTENT,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except UserAddress.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Address not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

# view for business profile
class BusinessProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                business_profile = BusinessProfile.objects.get(pk=pk)
                serializer = BusinessProfileSerializer(business_profile)
                return Response(
                    {
                        "success": True,
                        "msg": "Business profile retrieved successfully.",
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except BusinessProfile.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Business profile not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            business_profiles = BusinessProfile.objects.all()
            serializer = BusinessProfileSerializer(business_profiles, many=True)
            return Response(
                {
                    "success": True,
                    "msg": "Business profiles retrieved successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def post(self, request, format=None):
        serializer = BusinessProfileSerializer(data=request.data)
        if serializer.is_valid():
            if BusinessProfile.objects.filter(
                user=request.data["user"],
                businessEmail=request.data["businessEmail"],
            ).exists():
                return Response(
                    {
                        "success": False,
                        "msg": "Business profile with this email already exists.",
                        "status": status.HTTP_409_CONFLICT,
                    },
                    status=status.HTTP_409_CONFLICT,
                )
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Business profile created successfully.",
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

    def patch(self, request, pk, format=None):
        try:
            business_profile = BusinessProfile.objects.get(pk=pk)
        except BusinessProfile.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Business profile not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = BusinessProfileSerializer(
            business_profile, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Business profile updated successfully.",
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
            business_profile = BusinessProfile.objects.get(pk=pk)
            business_profile.delete()
            return Response(
                {
                    "success": True,
                    "msg": "Business profile deleted successfully.",
                    "status": status.HTTP_204_NO_CONTENT,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except BusinessProfile.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Business profile not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# oprating hours view
class OperatingHoursView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = OperatingHoursSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Operating hours created successfully.",
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
                operating_hours = OperatingHours.objects.get(pk=pk)
                serializer = OperatingHoursSerializer(operating_hours)
                return Response(
                    {
                        "success": True,
                        "msg": "Operating hours retrieved successfully.",
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    },
                    status=status.HTTP_200_OK,
                )
            except OperatingHours.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "msg": "Operating hours not found.",
                        "status": status.HTTP_404_NOT_FOUND,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            operating_hours = OperatingHours.objects.all()
            serializer = OperatingHoursSerializer(operating_hours, many=True)
            return Response(
                {
                    "success": True,
                    "msg": "Operating hours retrieved successfully.",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            operating_hours = OperatingHours.objects.get(pk=pk)
        except OperatingHours.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Operating hours not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = OperatingHoursSerializer(
            operating_hours, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "Operating hours updated successfully.",
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
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        try:
            operating_hours = OperatingHours.objects.get(pk=pk)
            operating_hours.delete()
            return Response(
                {
                    "success": True,
                    "msg": "Operating hours deleted successfully.",
                    "status": status.HTTP_204_NO_CONTENT,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except OperatingHours.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "msg": "Operating hours not found.",
                    "status": status.HTTP_404_NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# logout user
# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, format=None):
#         try:
#             refresh_token = request.data["refresh"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(
#                 {
#                     "success": True,
#                     "msg": "Logged out successfully.",
#                     "status": status.HTTP_200_OK,
#                 },
#                 status=status.HTTP_200_OK,
#             )
#         except Exception as e:
#             return Response(
#                 {
#                     "success": False,
#                     "msg": "Logout failed. Invalid token.",
#                     "status": status.HTTP_400_BAD_REQUEST,
#                 },
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
