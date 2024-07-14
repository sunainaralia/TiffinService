from django.urls import path, include

urlpatterns = [
    path("user/", include("v1.api.Auth.urls")),
    path("kitchen/", include("v1.api.kitchen.urls")),
]
