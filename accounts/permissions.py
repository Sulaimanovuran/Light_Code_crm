from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsMentor(BasePermission):
    # CREATE, LIST
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user.is_authenticated and request.user.is_staff

    # UPDATE, DELETE, RETRIEVE
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_staff