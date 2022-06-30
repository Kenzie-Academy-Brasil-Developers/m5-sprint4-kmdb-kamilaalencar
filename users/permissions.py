from rest_framework import permissions

class UserCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return (
                request.user.is_authenticated
            and request.user.is_superuser
            )
        return True