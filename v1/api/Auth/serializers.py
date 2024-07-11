from rest_framework import serializers
from .models import UserProfile, UserAddress, BusinessProfile


# userprofile serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "username",
            "email",
            "phone_no",
            "is_admin",
            "is_superuser",
            "is_active",
            "is_blocked",
            "is_customer",
            "created_at",
            "updated_at",
            "recentLogin",
            "gender",
            "date_of_birth",
            "profile_photo",
        ]


# serializer for user login
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["phone_no"]


# serializer for adress details
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = [
            "id",
            "title",
            "user",
            "street",
            "city",
            "state",
            "pincode",
            "country",
        ]


# serializer for business profileclass :
class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = [
            "id",
            "user",
            "kitchenName",
            "businessEmail",
            "businessPhone",
            "street",
            "city",
            "state",
            "postalCode",
            "country",
            "latitude",
            "longitude",
            "facebook_link",
            "twitter_link",
            "instagram_link",
        ]
