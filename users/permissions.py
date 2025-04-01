from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """Проверка активности сотрудника"""
    def has_permission(self, request, view):
        if request.user.is_active and request.user.is_staff:
            return True
        return False

