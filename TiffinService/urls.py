from django.contrib import admin
from django.urls import path,include
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
class welcomeApi(APIView):

    def get(self, request, pk=None, format=None):
        return Response({"msg": "welcome to Tiffin service"})


urlpatterns = [
    path("", welcomeApi.as_view()),
    path("admin/", admin.site.urls),
    path("v1/",include('v1.urls'))
]
urlpatterns+=staticfiles_urlpatterns()