from rest_framework.permissions import IsAuthenticated


class IsStaff(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        status = super().has_object_permission(request, view, obj)

        return status and request.user.is_staff


class IsOwner(IsStaff):
    def has_object_permission(self, request, view, obj):
        if not (obj.owner == request.user) or not super().has_object_permission(
            request, view, obj
        ):
            return False
        return True
