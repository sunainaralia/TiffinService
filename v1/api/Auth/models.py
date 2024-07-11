from django.db import models


# UserProfile model
class UserProfile(models.Model):
    username = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    profile_photo = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    gender=models.CharField(max_length=100,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    recentLogin = models.DateTimeField(auto_now=True)
    is_blocked = models.BooleanField(default=False)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(null=True)
    is_customer=models.BooleanField(default=True)

# user address model
class UserAddress(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='address')
    title = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}: {self.street}, {self.city}, {self.state}, {self.country} - {self.pincode}"

    # model for business profile class BusinessProfile(models.Model):


class BusinessProfile(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="business_profiles"
    )
    kitchenName = models.CharField(max_length=255)
    businessEmail = models.EmailField(max_length=255)
    businessPhone = models.CharField(max_length=15)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    facebook_link = models.URLField(max_length=200, blank=True)
    twitter_link = models.URLField(max_length=200, blank=True)
    instagram_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.kitchenName} - {self.businessEmail}"


# models for oprating hours
class OperatingHours(models.Model):
    kitchen_id = models.ForeignKey(
        BusinessProfile, related_name="operating_hours", on_delete=models.CASCADE
    )
    monday = models.CharField(max_length=20)
    tuesday = models.CharField(max_length=20)
    wednesday = models.CharField(max_length=20)
    thursday = models.CharField(max_length=20)
    friday = models.CharField(max_length=20)
    saturday = models.CharField(max_length=20)
    sunday = models.CharField(max_length=20)
