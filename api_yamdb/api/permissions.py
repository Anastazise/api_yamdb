from rest_framework import permissions


class IsAuthorOrStaff(permissions.BasePermission):
    """
    permission to allow owners, admins and moderators to edit and delete objects.
    """
    def has_object_permission(self, request, view, obj):
        print(request.user)
        return obj.author == request.user or request.user.is_staff
