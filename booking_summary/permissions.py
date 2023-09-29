from rest_framework import permissions

class IsAuthorToViewReceipt(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Checks if the user is the author of the booking summary.
        return obj.user == request.user
