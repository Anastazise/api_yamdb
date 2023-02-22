from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    permission to allow admins and moderators to edit and delete objects.
    Other users can use only safe methods
    """
    def has_object_permission(self, request, view, obj):
        if request.user == AnonymousUser():
            value = False
        else:
            value = request.user.is_admin
        return (
            request.method in permissions.SAFE_METHODS
            or value
        )

    def has_permission(self, request, view):
        if request.user == AnonymousUser():
            value = False
        else:
            value = request.user.is_admin

        return (
            request.method in permissions.SAFE_METHODS
            or value
        )


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
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
