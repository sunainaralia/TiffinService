from django.contrib import admin
from .models import UserProfile, UserAddress, BusinessProfile, OperatingHours


# user profile admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
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


admin.site.register(UserProfile, UserProfileAdmin)


# admin for user address
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "user",
        "street",
        "city",
        "state",
        "pincode",
        "country",
    ]


admin.site.register(UserAddress, AddressAdmin)


# admin for business profile
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = [
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


admin.site.register(BusinessProfile, BusinessProfileAdmin)


# admin for oprating hours
class OperatingHoursAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "kitchen_id",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    )


admin.site.register(OperatingHours, OperatingHoursAdmin)
