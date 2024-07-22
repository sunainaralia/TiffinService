from django.urls import path
from .views import UserProfileView, SendOtpToMobileNo, LoginUserView,AddressView,BusinessProfileView,OperatingHoursView,LogoutView

urlpatterns = [
    path("", UserProfileView.as_view(), name="register"),
    path("<pk>/", UserProfileView.as_view(), name="register-detail"),
    path("sendOtp/", SendOtpToMobileNo.as_view()),
    path("login/<pk>/<otp>/", LoginUserView.as_view()),
    path("address/", AddressView.as_view()),
    path("address/<pk>/", AddressView.as_view()),
    path("business_profile/", BusinessProfileView.as_view()),
    path("business_profile/<pk>/", BusinessProfileView.as_view()),
    path("operating-hours/", OperatingHoursView.as_view()),
    path("operating-hours/<pk>/", OperatingHoursView.as_view()),
    path("logout/", LogoutView.as_view(), name="logout"),
]
