from django.urls import path, include


urlpatterns = [
    path(
        path("user/", include("v1.api.urls")),
        
    ),
]
