from rest_framework import permissions


class IsAuthorOrStaff(permissions.BasePermission):
    """
    permission to allow owners, admins and moderators
    to edit and delete objects.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_staff


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    !!! ПОМЕТКА !!! Нужно исправить, когда Настя пропишет виды пользователей
    permission to allow admins and moderators to edit and delete objects.
    Other users can use only safe methods
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_staff
        )
