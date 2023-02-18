from rest_framework import permissions


class IsAuthorOrStaff(permissions.BasePermission):
    """
    permission to allow owners, admins and moderators
    to edit and delete objects.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_moderator or request.user.is_admin


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    permission to allow admins and moderators to edit and delete objects.
    Other users can use only safe methods
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_admin
        )


class IsAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser)


class IsAuthorAdminModeratorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin
                or request.user.is_moderator
                or obj.author == request.user)

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)
