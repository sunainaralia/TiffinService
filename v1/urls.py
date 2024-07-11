from django.urls import path, include


urlpatterns = [
    path(
        path("api/", include("v1.api.urls")),
    ),
]
