from rest_framework.permissions import BasePermission


class IsAuthenticatedOrAllowedGet(BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user and request.user.is_authenticated
