from rest_framework.permissions import BasePermission

class CanCreateTicket(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class CanViewTicket(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.is_admin_role:
            return True

        if user.is_resolver:
            return obj.assigned_to == user

        return obj.created_by == user


class CanAssignTicket(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin_role


class CanChangeStatus(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.is_admin_role:
            return True

        if user.is_resolver:
            return obj.assigned_to == user

        return False
